from gmail_manager import user_name, user_password
import smtplib
import time
import gspread
from gservice_manager import credentials
from gservice_manager import gc


def send_email(to_address, content):
    print("\n\nSMTP gmail server login started:")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    print("Logging in as", user_name)
    server.login(user_name, user_password)
    print("Success")

    print("\nCreating message:")
    message = "Subject: MetLife Zrt. (Győr)\n\n"
    message += content
    message = message.encode("utf-8")
    print("Success")

    print("\nSending email as", user_name, "to", to_address)
    server.sendmail(user_name, to_address, message)
    print("Email sent successfully to", to_address)

    server.quit()
    print("Logging out and exiting SMTP gmail server")
    # Sleep for one second - avoiding losing connection and errors with SMTP server
    time.sleep(1)
    ("Done")


# Authorize the gspread library with the credentials
def authorize_gspread():
    gc = gspread.authorize(credentials)
    return gc


def open_google_sheet(spreadsheet, worksheet):
    if authorize_gspread():
        sheet = gc.open(spreadsheet).worksheet(worksheet)
    return sheet


def get_email_content_from_template():
    # Open the email template file and return its content with replaced placeholders as a string.
    with open("email_template.txt", "r", encoding="utf-8") as f:
        content = f.read()
