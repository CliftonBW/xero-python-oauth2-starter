from datetime import datetime, timedelta
import requests
import config
import logging
BILL_TOWN_URL = config.BILL_TOWN_URL
LOCAL_URL = config.LOCAL_URL
entity_invoices_code = config.ENTITY_INVOICES_CODE
invoice_code = config.INVOICE_CODE
post_invoice_code = config.POST_CODE
invoices_code = config.INVOICES_CODE
lineitem_code = config.LINEITEM_CODE
statement_code = config.STATEMENT_CODE
update_code = config.UPDATE_CODE
email_code = config.EMAIL_CODE
ENV = config.ENV
url = ""

if ENV == "development":
    url=LOCAL_URL
else:
    url=BILL_TOWN_URL



def getBillTownInvoices():
    req = requests.get(url + 'GetInvoices',params={"code":invoices_code})
    data = req.json()['data']
    return data

def getBillTownInvoice(id,PartitionKey):
    req = requests.get(url + 'GetInvoice',params={"invoice_number": id,"date": PartitionKey,"code":invoice_code})
    data = req.json()['data']
    return data

def getBillTownInvoicesByBWEntity(bill_entity): 
    today = datetime.utcnow()
    first = today.replace(day=1)
    PartitionKey = f"{first.strftime('%b_%Y')}_Invoice"
    req = requests.get(url + 'GetInvoicesByBWEntity',params={"bill_entity": bill_entity,"PartitionKey": PartitionKey,"code":entity_invoices_code})
    invoicesbyentity = req.json()['invoicedata']
    invoicesbyentitylineitem = req.json()['lineitemdata']
    return invoicesbyentity,invoicesbyentitylineitem

def updateBillTownInvoice(updatedict,bill_entity):
    today = datetime.utcnow()
    first = today.replace(day=1)
    PartitionKey = f"{first.strftime('%b_%Y')}_Invoice"
    req = requests.post(url + 'UpdateInvoice',params={"bill_entity": bill_entity,"PartitionKey": PartitionKey,"code":update_code},data=updatedict)

def getBillTownInvoiceLineItems(id,lineitemdate):
    req = requests.get(url + 'GetInvoiceLineItems',params={"invoice_number": id,"date": lineitemdate,"code":lineitem_code})
    logging.info(req)
    lineitems = req.json()['data']
    
    return lineitems

def getBillTownStatementByCompany(account_name):  
    req = requests.get(url + 'GetStatementByCompany',params={"invoice_number": account_name,"code":statement_code})
    data = req.json()['data']
    return data

def postBillTownInvoice(PartitionKey,id):
    req = requests.post(url + 'PostInvoice',params={"invoice_number": id,"code":post_invoice_code,"date":PartitionKey})
    data = req.json()['data']
    return data

def sendEmailBillTownInvoice(PartitionKey,id):
    req = requests.post(url + 'SendInvoiceEmail',params={"invoice_number": id,"code":email_code,"date": PartitionKey}) 

def previewBillTownInvoice(month,invoice_number):
    res = requests.get(url + 'GetInvoicePDF', stream=True, params={ "month": month, "invoice_number": invoice_number})
    return res

def previewBillTownStatement(month,bill_to):
    res = requests.get(url + 'GetStatementPDF', stream=True, params={ "month": month, "bill_to": bill_to})
    return res