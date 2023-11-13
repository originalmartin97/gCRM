# 'Tis but a script for the purpose of sending out emails to new potential customers using a Gmail account and a predefined Google Service Account.

# The magic starts here.
import functions as f

# Authenticate the service account.
f.authenticate_gservice_account()

# Load the data from the json file.
data = f.json_data_loader("spreadsheet_keys.json")

# Get gmail account credentials.
account = f.json_data_loader("gmail_credentials.json")

sheet = f.open_by_key_google_sheet(
    spreadsheet=data["sheets_customer_trgt"],
    worksheet=data["worksheets_insurance_name"],
)

# Check the sheet for new potential customers.
# If the 6th column is empty, send them an email via send_email() function.
for i, row in enumerate(sheet.get_all_values(), start=1):
    try:
        if not row[3]:
            f.send_email(
                row[2],
                f.create_email_content("templates/credit_template.txt", row[0]),
                account["username"],
                account["password"],
            )
            # Mark the customer as contacted.
            sheet.update_cell(i, 4, "igen")
            print("Ügyfél:", row[0], "sikeresen értesítve.")
        # If there is not one, do nothing.
    except Exception as e:
        print("An error occurred:", e)
        break  # Stop the script
