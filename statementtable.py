# import things
from flask_table import Table, Col, LinkCol, ButtonCol
import requests

# Declare your table
class StatementTable(Table):
    table_id = "data"
    classes = ['table table-striped']
    usage_allowance_type = Col('Data Type')
    service_details = Col('Service ID')
    local_site = Col('Local Site')
    router = Col('Router Name')
    usage = Col('Data Usage (GB)')
    allowance = Col('Allowance (GB)')
    overage = Col('Overage (GB)')
    dp_id = Col(' Data Pool ID')

# Get some objects
class StatementObject(object):
    def __init__(self, data): 
        self.PartitionKey = data.get("PartitionKey") 
        self.RowKey = data.get("RowKey") 
        self.id = data.get("id") 
        self.account_id = data.get("account_id") 
        self.service_details = data.get("service_details") 
        self.usage_allowance_type = data.get("usage_allowance_type") 
        self.local_site = data.get("local_site") 
        self.router = data.get("router") 
        self.status = data.get("status") 
        self.allowance = data.get("allowance") 
        self.usage = data.get("usage") 
        self.overage = data.get("overage") 
        self.start_invoice_date = data.get("start_invoice_date") 
        self.endbilldate = data.get("endbilldate") 
        self.dp_id = data.get("dp_id") 





