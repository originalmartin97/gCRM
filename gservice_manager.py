from google.oauth2 import service_account

# Define the scopes and credentials
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = service_account.Credentials.from_service_account_file(
    "gserviceaccount.json",
    scopes=scopes,
)
