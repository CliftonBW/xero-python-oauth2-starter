# -*- coding: utf-8 -*-
import logging
import os
from functools import wraps
from io import BytesIO
from logging.config import dictConfig
from wsgiref import headers
from flask import Flask, url_for, render_template, session, redirect,request, json, send_file
from flask_oauthlib.contrib.client import OAuth, OAuth2Application
from flask_session import Session
from flask_table import Table, Col
import requests
import logging_settings
from invoicetable import InvoiceTable, InvoiceItem
from lineitemtable import LineItemTable, LineItemObject
from statementtable import StatementTable, StatementObject
import identity, identity.web
import config
dictConfig(logging_settings.default_settings)

# configure main flask application
app = Flask(__name__)
app.config.from_object("default_settings")
app.config.from_pyfile("config.py", silent=True)
url = ""
if app.config["ENV"] == "development":
    url=app.config["LOCAL_URL"]
else:
    url=app.config["BILL_TOWN_URL"]
    # allow oauth2 loop to run over http (used for local testing only)
#os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

# configure persistent session cache
Session(app)

# This section is needed for url_for("foo", _external=True) to automatically
# generate http scheme when this sample is running on localhost,
# and to generate https scheme when it is deployed behind reversed proxy.
# See also https://flask.palletsprojects.com/en/1.0.x/deploying/wsgi-standalone/#proxy-setups
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

auth = identity.web.Auth(
    session=session,
    authority=app.config.get("AUTHORITY"),
    client_id=app.config["CLIENT_ID"],
    client_credential=app.config["CLIENT_SECRET"],
    )

@app.route("/login")
def login():
    return render_template("login.html", version=identity.__version__, **auth.log_in(
        scopes=config.SCOPE,  # Have user consent scopes during log-in
        redirect_uri=url_for("auth_response", _external=True),  # Optional. If present, this absolute URL must match your app's redirect_uri registered in Azure Portal
        ))

@app.route(config.REDIRECT_PATH)
def auth_response():
    result = auth.complete_log_in(request.args)
    return render_template("auth_error.html", result=result) if "error" in result else redirect(url_for("index"))

@app.route("/logout")
def logout():
    return redirect(auth.log_out(url_for("index", _external=True)))

# @app.route("/")
# def index():
#     if not auth.get_user():
#         return redirect(url_for("login"))
#     return render_template('index.html', user=auth.get_user(), version=identity.__version__)

@app.route("/call_downstream_api")
def call_downstream_api():
    token = auth.get_token_for_user(config.SCOPE)
    if "error" in token:
        return redirect(url_for("login"))
    api_result = requests.get(  # Use token to call downstream api
        config.ENDPOINT,
        headers={'Authorization': 'Bearer ' + token['access_token']},
        ).json()
    return render_template('display.html', result=api_result)



@app.route("/")
def index():
    if not auth.get_user():
        return redirect(url_for("login"))
    code=app.config["INVOICES_CODE"]
    req = requests.get(url + 'GetInvoices',params={"code":code})
    data = req.json()['data']
    items = []
    for d in data:
        items.append(InvoiceItem(data=d))

    table = InvoiceTable(items)
    return render_template(
        "table.html",
        title="Invoices",
        table=table
    )


@app.route("/post-invoice/<string:PartitionKey>/<string:id>")
def post_invoice(PartitionKey,id):
    post_code=app.config["POST_CODE"]  
    req4 = requests.get(url + 'PostInvoice',params={"invoice_number": id,"code":post_code})
    return redirect(url_for("get_lineitems", id=id,PartitionKey=PartitionKey))


@app.route("/send-email/<string:PartitionKey>/<string:id>")
def send_email(PartitionKey,id):
    invoice_code=app.config["INVOICE_CODE"]
    email_code=app.config["EMAIL_CODE"] 
    req2 = requests.get(url + 'GetInvoice',params={"invoice_number": id,"date": PartitionKey,"code":invoice_code})
    invoice = req2.json()['data']   
    id = ""
    for details in invoice:
        id = details.get("id")
        PartitionKey = details.get("PartitionKey")
    req3 = requests.get(url + 'SendInvoiceEmail',params={"invoice_number": id,"code":email_code})   
    return redirect(url_for("get_lineitems", id=id,PartitionKey=PartitionKey))

@app.route("/get-lineitems/<string:PartitionKey>/<string:id>")
def get_lineitems(PartitionKey,id):
    lineitemcode=app.config["LINEITEM_CODE"]
    invoicecode=app.config["INVOICE_CODE"]
    lineitemdate = PartitionKey.replace('Invoice','Lineitem')
    req = requests.get(url + 'GetInvoiceLineItems',params={"invoice_number": id,"date": lineitemdate,"code":lineitemcode})
    data = req.json()['data']
    req2 = requests.get(url + 'GetInvoice',params={"invoice_number": id,"date": PartitionKey,"code":invoicecode})
    data2 = req2.json()['data']
    items = []

    for d in data:
        items.append(LineItemObject(data=d))

    table = LineItemTable(items)
    return render_template(
        "lineitemtable.html",
        id=id,
        PartitionKey=PartitionKey,
        table=table,
        invoices=data2
    )

@app.route("/get-statements/<string:account_name>")
def get_statements(account_name):
    statementcode=app.config["STATEMENT_CODE"]
    invoicecode=app.config["INVOICE_CODE"]
    req = requests.get(url + 'GetStatementByCompany',params={"invoice_number": account_name,"code":statementcode})
    data = req.json()['data']
    req2 = requests.get(url + 'GetInvoice',params={"invoice_number": id,"code":invoicecode})
    data2 = req2.json()['data']
    items = []

    for d in data:
        items.append(StatementObject(data=d))

    table = StatementTable(items)
    return render_template(
        "lineitemtable.html",
        id=id,
        table=table,
        invoices=data2
    )

@app.route("/preview_invoice/<string:PartitionKey>/<string:invoice_number>")
def preview_invoice(PartitionKey: str, invoice_number: str):
    month = PartitionKey.replace("_Invoice", "")
    res = requests.get(url + 'GetInvoicePDF', stream=True, params={ "month": month, "invoice_number": invoice_number})

    if res.status_code == 200:
        return send_file(res.raw, mimetype='application/pdf', as_attachment=False, download_name=f"{invoice_number} - Invoice.pdf")
    else:
        return "Failed to download the PDF."

@app.route("/preview_statement/<string:PartitionKey>/<string:bill_to>")
def preview_statement(PartitionKey: str, bill_to: str):
    month = PartitionKey.replace("_Invoice", "")
    res = requests.get(url + 'GetStatementPDF', stream=True, params={ "month": month, "bill_to": bill_to})

    if res.status_code == 200:
        return send_file(res.raw, mimetype='application/pdf', as_attachment=False, download_name=f"{bill_to} - Service Statement.pdf")
    else:
        return "Service Statement does not exist."


@app.route("/get-invoices-azure")
def get_invoices_azure():
    code=app.config["INVOICES_CODE"]
    req = requests.get(url + 'GetInvoices',params={"code":code})
    data = req.json()['data']
    items = []
    for d in data:
        items.append(InvoiceItem(data=d))

    table = InvoiceTable(items)
    return render_template(
        "table.html",
        title="Invoices",
        table=table
    )

if __name__ == "__main__":
    app.run(host='localhost')
