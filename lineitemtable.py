# import things
from flask_table import Table, Col, LinkCol, ButtonCol
import requests

# Declare your table
class LineItemTable(Table):
    table_id = "lineitemdata"
    classes = ['table table-striped']
    description = Col('Description')
    order_id = Col('Order ID')
    service_id = Col('Service ID')
    purchase_order = Col('Purchase Order')
    service_details = Col('Service Details')
    pool_id = Col('Pool ID')
    quantity = Col('Quantity')
    unit_amount = Col('Unit Amount')
    lineitem_total_amount = Col('Lineitem Total Amount')
    tax_type = Col('Tax Type')


# Get some objects
class LineItemObject(object):
    def __init__(self, data): 
        self.PartitionKey = data.get("PartitionKey") 
        self.RowKey = data.get("RowKey") 
        self.id = data.get("id") 
        self.account_id = data.get("account_id") 
        self.account_name = data.get("account_name") 
        self.account_code = data.get("account_code") 
        self.tax_type = data.get("tax_type") 
        self.discount = data.get("discount") 
        self.currency = data.get("currency") 
        self.site_country = data.get("site_country") 
        self.local_site = data.get("local_site") 
        self.sub_account_name = data.get("sub_account_name") 
        self.attention = data.get("attention") 
        self.primary_finance_email = data.get("primary_finance_email") 
        self.finance_email = data.get("finance_email")
        self.billing_street = data.get("billing_street") 
        self.billing_state = data.get("billing_state") 
        self.billing_code = data.get("billing_code") 
        self.billing_city = data.get("billing_city") 
        self.floor_unit = data.get("floor_unit") 
        self.invoice_number = data.get("invoice_number") 
        self.invoice_owner = data.get("invoice_owner") 
        self.invoice_owner_email = data.get("invoice_owner_email") 
        self.separate_order = data.get("separate_order") 
        self.is_termination = data.get("is_termination") 
        self.description = data.get("description")
        self.order_id = data.get("order_id")
        self.service_id = data.get("service_id")
        self.purchase_order = data.get("purchase_order")
        self.billing_period = data.get("billing_period")
        self.service_details = data.get("service_details")
        self.quantity = data.get("quantity")
        self.unit_amount = data.get("unit_amount")
        self.lineitem_total_amount = data.get("lineitem_total_amount")
        self.pro_rated_allowance_qnty = data.get("pro_rated_allowance_qnty")
        self.start_invoice_date = data.get("start_invoice_date")
        self.start_bill_date = data.get("start_bill_date")
        self.end_bill_date = data.get("end_bill_date")
        self.line_item_id = data.get("line_item_id")
        self.payment_term = data.get("payment_term")
        self.circuit_id = data.get("circuit_id")
        self.charge_type = data.get("charge_type")
        self.invoice_format = data.get("invoice_format")
        self.key = data.get("key")
        self.internal_invoice_number = data.get("internal_invoice_number")
        self.is_data_pdt = data.get("is_data_pdt")
        self.is_overage_pdt = data.get("is_overage_pdt")
        self.is_latest_so = data.get("is_latest_so")
        self.pool_id = data.get("pool_id")
        self.allowance = data.get("allowance")
        self.product_id = data.get("product_id")


