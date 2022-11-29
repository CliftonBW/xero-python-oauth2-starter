import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
LINEITEM_CODE = os.getenv('LINEITEM_CODE')
INVOICE_CODE = os.getenv('INVOICE_CODE')
EMAIL_CODE = os.getenv('EMAIL_CODE')
INVOICES_CODE = os.getenv('INVOICES_CODE')
POST_CODE = os.getenv('POST_CODE')
UPDATE_CODE = os.getenv('UPDATE_CODE')
BILL_TOWN_URL = os.getenv('BILL_TOWN_URL')
LOCAL_URL = os.getenv('LOCAL_URL')
ENV = os.getenv('ENV')
