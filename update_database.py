# 'Tis but a script for the purpose of updating the database with new potential customers using google Sheets and a predefined Google Service Account.

# The magic starts here.
from gservice_manager import gc
import functions as f
import doc_list as dl


# Open source sheet.
source_sheet = f.open_google_sheet(
    spreadsheet=dl.sheets_customer_src, worksheet=dl.worksheets_credit_name
)
# Copy the rows to a temporary list.
temp_list = source_sheet.get_all_values()
# Close the source sheet.
source_sheet = None
# Open target sheet.
target_sheet = f.open_google_sheet(
    spreadsheet=dl.sheets_customer_trgt, worksheet=dl.worksheets_credit_name
)
# Iterate through the temporary list (check the name column).
for i, row in enumerate(temp_list, start=1):
    print("Ügyfél ellenőrzése:", row[0])
    # If there is a new name, add it to the target sheet as a new row.
    if not row[0] in target_sheet.col_values(1):
        target_sheet.append_row(row)
        print("Új ügyfél felvéve:", row[0])
