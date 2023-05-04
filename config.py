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
TENANT_NAME= os.getenv('TENANT_NAME')

AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
# AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

REDIRECT_PATH = "/auth-end.html"  # Used for forming an absolute URL to your redirect URI.
                              # The absolute URL must match the redirect URI you set
                              # in the app's registration in the Azure portal.

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.ReadBasic.All"]

SESSION_TYPE = "filesystem"  # Specifies the token cache should be stored in server-side session