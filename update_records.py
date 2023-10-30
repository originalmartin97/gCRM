from google.oauth2 import service_account
import gspread
import time

# Define the scopes and credentials
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = service_account.Credentials.from_service_account_file(
    "metlifeautomatizationsystem-5dcf21488d37.json",
    scopes=scopes,
)

# Authorize the gspread library with the credentials
gc = gspread.authorize(credentials)

# Define the folder ID and spreadsheet keys
folderID = "1Cs_e2kBo8TXj1Skx44Q41ivTWOAmQyc4"
source_spreadsheet_key = "1w0Hx7qlgfLTpjFS7s7g6VkhtntAEIDeERixw1_zUpuA"
target_spreadsheet_key = "1qDk26o-W9CGCZ-qrLLNYRziOjLTn9A1ij80JeNxiCpQ"


# Open one of the spreadsheets
source_spreadsheet = gc.open_by_key(source_spreadsheet_key)
# Wait for 5 seconds to avoid API call quota limit
time.sleep(5)
target_spreadsheet = gc.open_by_key(target_spreadsheet_key)


# Get the worksheets from the spreadsheets
source_worksheet = source_spreadsheet.worksheet("Baleset")
target_worksheet = target_spreadsheet.worksheet("Baleset")

# Iterate through first column of source worksheet
source_values_list = source_worksheet.col_values(1)
print(source_values_list)

# Iterate through first column of target worksheet
target_values_list = target_worksheet.col_values(1)
print(target_values_list)
