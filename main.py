import csv
import smtplib
import os
import time

UserName = "originalmartin97@gmail.com"
UserPassword = "zklybkojdcacniof"
IOFilePathInsurance = (
    "/home/martin/projects/mailing_list_insurance/potential_customers_insurance.csv"
)
IOFilePathCredit = (
    "/home/martin/projects/mailing_list_insurance/potential_customers_credit.csv"
)
IOFilePathPension = (
    "/home/martin/projects/mailing_list_insurance/potential_customers_pension.csv"
)


# This code only uses csv and txt formatted files as source.


# Sends an email to the specified address with the specified name and content as message.


def send_email(recipients, content):
    print("\n\nSmtp gmail server login started:")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    print("Logging in as", UserName)
    server.login(UserName, UserPassword)
    print("Success")

    print("\nCreating message:")
    message = "Subject: MetLife Zrt. (Győr)\n\n"
    message += content
    message = message.encode("utf-8")
    print("Success")

    # Join the recipients as a comma-separated string for the "To" field
    to_address = ", ".join(recipients)

    print("\nSending email as", UserName, "to", to_address)
    server.sendmail(UserName, to_address, message)
    print("Email sent successfully to", to_address)

    server.quit()
    print("Logging out and exiting smtp gmail server")
    time.sleep(1)
    ("Done")


def sendMailInsurance():
    recipients_and_names = []

    # Reads in the template content from file
    with open(
        "/home/martin/projects/mailing_list_insurance/insurance_template.txt", "r"
    ) as template:
        template_content = template.read()

    # Checks if file exists
    if os.path.isfile(IOFilePathInsurance):
        # Opens the source file for reading and writing
        with open(IOFilePathInsurance, "r+") as IOFile:
            # Initiates variable for containing the rows of the source file
            lines = []

            reader = csv.reader(IOFile, delimiter=",")

            # Iterates through rows of the source file
            for row in reader:
                # Checks if the email hasn't already been sent out to the customer
                if row[2] != "Sent":
                    email = row[1]
                    name = row[0]

                    # Append recipient and name as a tuple
                    recipients_and_names.append((email, name))

                # Appends the current row to the lines container
                lines.append(row)

            IOFile.close()

        template.close()

        # Send emails to all recipients with their personalized content
        for email, name in recipients_and_names:
            # Create personalized content for each email
            content = template_content.format(name)

            # Send the email with personalized content
            send_email([email], content)

        # Deletes the source file beforehand
        os.remove(IOFilePathInsurance)

        # Reopen the source file to update "Sent" flag
        with open(IOFilePathInsurance, "w", newline="") as newCsvFile:
            writer = csv.writer(newCsvFile, delimiter=",")

            # Write the rows to the source file using writerows()
            writer.writerows(lines)
            newCsvFile.close()


def sendMailCredit():
    recipients_and_names = []

    # Reads in the template content from file
    with open(
        "/home/martin/projects/mailing_list_insurance/credit_template.txt", "r"
    ) as template:
        template_content = template.read()

    # Checks if file exists
    if os.path.isfile(IOFilePathCredit):
        # Opens the source file for reading and writing
        with open(IOFilePathCredit, "r+") as IOFile:
            # Initiates variable for containing the rows of the source file
            lines = []

            reader = csv.reader(IOFile, delimiter=",")

            # Iterates through rows of the source file
            for row in reader:
                # Checks if the email hasn't already been sent out to the customer
                if row[2] != "Sent":
                    email = row[1]
                    name = row[0]

                    # Append recipient and name as a tuple
                    recipients_and_names.append((email, name))

                # Appends the current row to the lines container
                lines.append(row)

            IOFile.close()

        template.close()

        # Send emails to all recipients with their personalized content
        for email, name in recipients_and_names:
            # Create personalized content for each email
            content = template_content.format(name)

            # Send the email with personalized content
            send_email([email], content)

        # Deletes the source file beforehand
        os.remove(IOFilePathCredit)

        # Reopen the source file to update "Sent" flag
        with open(IOFilePathCredit, "w", newline="") as newCsvFile:
            writer = csv.writer(newCsvFile, delimiter=",")

            # Write the rows to the source file using writerows()
            writer.writerows(lines)
            newCsvFile.close()


def sendMailPension():
    recipients_and_names = []

    # Reads in the template content from file
    with open(
        "/home/martin/projects/mailing_list_insurance/pension_template.txt", "r"
    ) as template:
        template_content = template.read()

    # Checks if file exists
    if os.path.isfile(IOFilePathPension):
        # Opens the source file for reading and writing
        with open(IOFilePathPension, "r+") as IOFile:
            # Initiates variable for containing the rows of the source file
            lines = []

            reader = csv.reader(IOFile, delimiter=",")

            # Iterates through rows of the source file
            for row in reader:
                # Checks if the email hasn't already been sent out to the customer
                if row[2] != "Sent":
                    email = row[1]
                    name = row[0]

                    # Append recipient and name as a tuple
                    recipients_and_names.append((email, name))

                # Appends the current row to the lines container
                lines.append(row)

            IOFile.close()

        template.close()

        # Send emails to all recipients with their personalized content
        for email, name in recipients_and_names:
            # Create personalized content for each email
            content = template_content.format(name)

            # Send the email with personalized content
            send_email([email], content)

        # Deletes the source file beforehand
        os.remove(IOFilePathPension)

        # Reopen the source file to update "Sent" flag
        with open(IOFilePathPension, "w", newline="") as newCsvFile:
            writer = csv.writer(newCsvFile, delimiter=",")

            # Write the rows to the source file using writerows()
            writer.writerows(lines)
            newCsvFile.close()


if __name__ == "__main__":
    print("Martin Marketing Mailing System")

    while True:
        userInput = input(
            "\n\n\nWhat do you want to do?\n\n0 - Exit program\n1 - Send out emails about insurance to potential customers\n2 - Send out emails about credit to potential customers\n"
        )

        if userInput == "1":
            sendMailInsurance()
        elif userInput == "2":
            sendMailCredit()
        elif userInput == "0":
            print("\n\nGoodbye! :)")
            quit()
