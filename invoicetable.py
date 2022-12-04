# import things
from flask_table import Table, Col, LinkCol, ButtonCol, BoolCol
import requests

# Declare your table
class InvoiceTable(Table):
    table_id = "invoicedata"
    classes = ['table table-striped'] 
    RowKey = Col('')
    invoice_number = Col('Invoice Number')
    LineItems = LinkCol('Line Items',endpoint="get_lineitems",url_kwargs=dict(id='id'),anchor_attrs={'class': 'btn btn-outline-primary btn-sm'})
    invoice_date = Col('Invoice Date')
    due_date = Col('Due Date')
    paid_amount = Col('Paid Amount')
    outstanding_amount = Col('Outstanding Amount')
    overdue_date = Col('Overdue Date')
    currency = Col('Currency')
    invoice_total_amount = Col('Invoice Total Amount')
    invoice_status = Col('Invoice Status')
    payment_status = Col('Payment Status')
    tax_type = Col('Tax Type')    
    bill_entity = Col('Bill Entity')
    bill_to = Col('Bill To')
    reference = Col('Reference')
    local_site = Col('Local Site')
    invoice_owner = Col('Invoice Owner')
    collection = Col('Collection')

# Get some objects
class InvoiceItem(object):
    def __init__(self, data):
        self.PartitionKey = data.get("PartitionKey") 
        self.RowKey = data["RowKey"]
        self.id = data["id"]
        self.checkbox = ""
        self.LineItems = data
        self.collection = data["collection"]
        self.bill_to = data["bill_to"]
        self.attention = data["attention"]
        self.billing_street = data["billing_street"]
        self.billing_state = data["billing_state"]
        self.billing_code = data["billing_code"]
        self.billing_city = data["billing_city"]
        self.floor_unit = data["floor_unit"]
        self.invoice_date = data["invoice_date"] if "invoice_date" in data else ""
        self.end_invoice_date = data["end_invoice_date"]
        self.reference = data.get("reference")
        self.due_date = data["due_date"]
        self.invoice_owner_email = data["invoice_owner_email"]
        self.invoice_owner = data["invoice_owner"]
        self.local_site = data["local_site"]
        self.description = data["description"]
        self.overdue_date = data["overdue_date"]
        self.paid_amount = data["paid_amount"]
        self.outstanding_amount = data["outstanding_amount"]
        self.invoice_total_amount = data["invoice_total_amount"]
        self.invoice_number = data["invoice_number"]
        self.invoice_status = data["invoice_status"]
        self.payment_status = data["payment_status"]
        self.tax_type = data.get("tax_type")
        self.currency = data["currency"]
        self.bill_entity = data["bill_entity"]
        self.sub_account = data["sub_account"]
        self.seperate_order = data["seperate_order"]
        self.invoice_number_key = data["invoice_number_key"]
        self.primary_finance_email = data["primary_finance_email"]
        self.finance_email = data["finance_email"]

