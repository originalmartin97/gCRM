# 'Tis but a script for the purpose of sending out emails to new potential customers using a Gmail account and a predefined Google Service Account.

# The magic starts here.
import json
from gmail_manager import user_name, user_password
import functions as f

# Use the given google sheet as a database.
from gservice_manager import gc

sheet = f.open_google_sheet(spreadsheet="valami", worksheet="valami")

# Check the sheet for new potential customers.
# If the 6th column is empty, send them an email via send_email() function.
for row in sheet.get_all_values():
    if not row[5]:  # 6th column, index is 5 because Python uses 0-based indexing
        f.send_email(row[3],)

# If there are any, send them an email.
# If the email was sent successfully, mark the customer as contacted.
# If there are not any, do nothing.
# If there is an error, print it out and stop the script.
