# import things
from flask_table import Table, Col, LinkCol, ButtonCol
import requests

# Declare your table
class LineItemTable(Table):
    table_id = "lineitemdata"
    classes = ['table table-striped lineitemdata']
    description = Col('Description',column_html_attrs={'name':'description'})
    order_id = Col('Order ID',column_html_attrs={'name':'order_id'})
    service_id = Col('Service ID',column_html_attrs={'name':'service_id'})
    local_site = Col('local_site',column_html_attrs={'hidden': 'true','name':'local_site'})
    purchase_order = Col('Purchase Order',column_html_attrs={'name':'purchase_order'})
    service_details = Col('Service Details',column_html_attrs={'name':'service_details'})
    pool_id = Col('Pool ID',column_html_attrs={'name':'pool_id'})
    quantity = Col('Quantity',column_html_attrs={'name':'quantity'})
    unit_amount = Col('Unit Amount',column_html_attrs={'name':'unit_amount'}) 
    tax_type = Col('Tax Type',column_html_attrs={'name':'tax_type'})
    lineitem_total_amount_with_tax = Col('Amount With Tax',column_html_attrs={'name':'lineitem_total_amount_with_tax'})
    lineitem_tax_amount = Col('lineitem_tax_amount',column_html_attrs={'hidden': 'true','name':'lineitem_tax_amount'})
    lineitem_total_amount = Col('lineitem_total_amount',column_html_attrs={'hidden': 'true','name':'lineitem_total_amount'})
    lineitem_discount_amount  = Col('lineitem_discount_amount',column_html_attrs={'hidden': 'true','name':'lineitem_discount_amount'})
    discount = Col('discount',column_html_attrs={'hidden': 'true','name':'discount'})
    start_invoice_date = Col('start_invoice_date',column_html_attrs={'hidden': 'true','name':'start_invoice_date'})
    start_bill_date = Col('start_bill_date',column_html_attrs={'hidden': 'true','name':'start_bill_date'})
    end_bill_date = Col('end_bill_date',column_html_attrs={'hidden': 'true','name':'end_bill_date'})
    termination_date = Col('termination_date',column_html_attrs={'hidden': 'true','name':'termination_date'})
    Child = Col('More Information',column_html_attrs={'class': 'dt-control .filter'})

# Get some objects
class LineItemObject(object):
    def __init__(self, data): 
        self.Child = ""
        self.PartitionKey = data.get("PartitionKey") 
        self.RowKey = data.get("RowKey") 
        self.id = data.get("id") 
        self.sales_order_internal_id = data.get("sales_order_internal_id") 
        self.account_code = data.get("account_code") 
        self.site_country = data.get("site_country") 
        self.order_id = data.get("order_id") 
        self.pool_id = data.get("pool_id") 
        self.local_site = data.get("local_site") 
        self.service_details = data.get("service_details") 
        self.internal_invoice_number = data.get("internal_invoice_number")      
        self.invoice_number = data.get("invoice_number") 
        self.is_latest_so = data.get("is_latest_so") 
        self.start_invoice_date = data.get("start_invoice_date") 
        self.start_bill_date = data.get("start_bill_date") 
        self.end_bill_date = data.get("end_bill_date") 
        self.termination_date = data.get("termination_date")
        self.is_termination = data.get("is_termination")
        self.circuit_id = data.get("circuit_id")
        self.our_services_internal_id = data.get("our_services_internal_id")
        self.product_name = data.get("product_name")
        self.charge_type = data.get("charge_type")
        self.xero_tracking = data.get("xero_tracking")
        self.product_id = data.get("product_id")
        self.product_category = data.get("product_category")
        self.product_description = data.get("product_description")
        self.line_item_id = data.get("line_item_id")
        self.unit_amount = data.get("unit_amount")
        self.quantity = data.get("quantity")
        self.discount = str(data.get("discount")) + "%"
        self.is_overage_pdt = data.get("is_overage_pdt")
        self.pro_rated_allowance_qnty = data.get("pro_rated_allowance_qnty")
        self.is_data_pdt = data.get("is_data_pdt")
        self.is_equipment = data.get("is_equipment")
        self.description = data.get("description")
        self.entity_name = data.get("entity_name")
        self.tax_display = data.get("tax_display")
        self.actual_invoice_tax_display = data.get("actual_invoice_tax_display")
        self.tax_type = data.get("tax_type")
        self.account_code_xero = data.get("account_code_xero")
        self.lineitem_total_amount = data.get("lineitem_total_amount")
        self.lineitem_total_amount_with_tax = data.get("lineitem_total_amount_with_tax")
        self.lineitem_tax_amount = data.get("lineitem_tax_amount")
        self.lineitem_discount_amount = data.get("lineitem_discount_amount")
        self.invoice_start = data.get("invoice_start")
        self.invoice_end = data.get("invoice_end")
        self.service_activation = data.get("service_activation")
        self.telco_tax_exempt = data.get("telco_tax_exempt")
        self.purchase_order = data.get("purchase_order")
        self.service_id = data.get("service_id")

