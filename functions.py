from gmail_manager import user_name, user_password
import smtplib
import time
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


def open_google_sheet(spreadsheet, worksheet):
    sheet = gc.open(spreadsheet).worksheet(worksheet)
    return sheet


def create_email_content(template, name):
    with open(template, "r") as template_file:
        content = template_file.read()
        content = content.replace("{{name}}", name)
    return content
