# import things
from flask_table import Table, Col, LinkCol, ButtonCol, BoolCol
import requests

# Declare your table
class InvoiceTable(Table):
    table_id = "invoicedata" 
    classes = ['table table-striped invoicedata'] 
    LineItems = LinkCol('Line Items',text_fallback='Line Item',endpoint="get_lineitems",url_kwargs=dict(PartitionKey='PartitionKey',id='id'),anchor_attrs={'class': 'btn btn-outline-primary btn-sm no-filter','target':'_blank'},)
    PartitionKey = Col('Invoice Month',th_html_attrs={'class': 'filter'},column_html_attrs={'name':'PartitionKey'})
    invoice_number = Col('Invoice Number',th_html_attrs={'class': 'filter'},column_html_attrs={'name':'invoice_number'})   
    bill_to = Col('Bill To',th_html_attrs={'class': 'filter'},column_html_attrs={'name':'bill_to'})
    primary_finance_email = Col('primary_finance_email',column_html_attrs={'hidden': 'true','name':'primary_finance_email'})
    finance_email = Col('finance_email',column_html_attrs={'hidden': 'true','name':'finance_email'})
    local_site = Col('Local Site',th_html_attrs={'class': 'filter'},column_html_attrs={'name':'local_site'})
    invoice_status = Col('Invoice Status',th_html_attrs={'class': 'filter'},column_html_attrs={'name':'invoice_status'})
    currency = Col('Currency',column_html_attrs={'name':'currency'})
    invoice_total_amount= Col('invoice_total_amount',column_html_attrs={'hidden': 'true','name':'invoice_total_amount'})
    invoice_tax_amount= Col('invoice_tax_amount',column_html_attrs={'hidden': 'true','name':'invoice_tax_amount'})
    invoice_total_amount_with_tax = Col('Invoice Total Amount With Tax',th_html_attrs={'class': 'filter'},column_html_attrs={'name':'invoice_total_amount_with_tax'}) 
    bill_entity = Col('Bill Entity',th_html_attrs={'class': 'filter'},column_html_attrs={'name':'bill_entity'})
    invoice_owner = Col('Invoice Owner',th_html_attrs={'class': 'filter'},column_html_attrs={'name':'invoice_owner'})     
    invoice_date = Col('Invoice Date',th_html_attrs={'class': 'filter'},column_html_attrs={'hidden': 'true','name':'invoice_date'})      
    due_date = Col('Due Date',column_html_attrs={'hidden': 'true','name':'due_date'})
    payment_status = Col('Payment Status',column_html_attrs={'hidden': 'true','name':'payment_status'})            
    paid_amount = Col('Paid Amount',column_html_attrs={'hidden': 'true','name':'paid_amount'})
    outstanding_amount = Col('Outstanding Amount',column_html_attrs={'hidden': 'true','name':'outstanding_amount'})
    collection  = Col('collection',column_html_attrs={'hidden': 'true','name':'collection'})
    Child = Col('More Info',column_html_attrs={'class': 'dt-control'}) 


class InvoiceItem(object):
    def __init__(self, data):
        self.PartitionKey = data.get("PartitionKey")
        self.RowKey = data.get("RowKey")
        self.id = data.get("id")
        self.Child = ""
        self.checkbox = ""
        self.LineItems = data.get("invoice_number")
        self.collection = data.get("collection")
        self.bill_to = data.get("bill_to")
        self.attention = data.get("attention")
        self.billing_street = data.get("billing_street")
        self.billing_state = data.get("billing_state")
        self.billing_code = data.get("billing_code")
        self.billing_city = data.get("billing_city")
        self.floor_unit = data.get("floor_unit")
        self.invoice_date = data.get("invoice_date")
        self.end_invoice_date = data.get("end_invoice_date")
        self.reference = data.get("reference")
        self.due_date = data.get("due_date")
        self.invoice_owner_email = data.get("invoice_owner_email")
        self.invoice_owner = data.get("invoice_owner")
        self.local_site = data.get("local_site")
        self.description = data.get("description")
        self.overdue_date = data.get("overdue_date")
        self.paid_amount = data.get("paid_amount")
        self.outstanding_amount = data.get("outstanding_amount")
        self.invoice_total_amount = data.get("invoice_total_amount")
        self.invoice_tax_amount = data.get("invoice_tax_amount")
        self.invoice_total_amount_with_tax = data.get("invoice_total_amount_with_tax")
        self.invoice_number = data.get("invoice_number")
        self.invoice_status = data.get("invoice_status")
        self.payment_status = data.get("payment_status")
        self.tax_type = data.get("tax_type")
        self.currency = data.get("currency")
        self.bill_entity = data.get("bill_entity")
        self.sub_account = data.get("sub_account")
        self.seperate_order = data.get("seperate_order")
        self.invoice_number_key = data.get("invoice_number_key")
        self.primary_finance_email = data.get("primary_finance_email")
        self.finance_email = data.get("finance_email")
