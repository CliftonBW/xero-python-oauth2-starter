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
ENV = os.getenv('ENV')
