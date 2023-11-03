from google.oauth2 import service_account
import gspread

# Define the scopes and credentials
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]
credentials = service_account.Credentials.from_service_account_file(
    "gserviceaccount.json",
    scopes=scopes,
)

gc = gspread.authorize(credentials)
