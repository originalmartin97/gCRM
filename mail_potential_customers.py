# 'Tis but a script for the purpose of sending out emails to new potential customers using a Gmail account and a predefined Google Service Account.

# The magic starts here.
from gmail_manager import user_name, user_password
import functions as f

# Use the given google sheet as a database.
from gservice_manager import gc

sheet = f.open_google_sheet(spreadsheet="Jelentkezők_Munkatábla1", worksheet="Teszt")

# Check the sheet for new potential customers.
# If the 6th column is empty, send them an email via send_email() function.
for i, row in enumerate(sheet.get_all_values(), start=1):
    try:
        if not row[6]:  # 7th column, index is 6 because Python uses 0-based indexing
            f.send_email(
                row[4],
                f.create_email_content("templates/insurance_template.txt", row[0]),
            )
            # Mark the customer as contacted.
            sheet.update_cell(i, 7, "igen")
            print("Ügyfél:", row[0], "sikeresen értesítve.")
        # If there is not one, do nothing.
    except Exception as e:
        print("An error occurred:", e)
        break  # Stop the script
