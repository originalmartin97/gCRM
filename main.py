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


# This code only uses csv and txt formatted files as source.


# Sends an email to the specified address with the specified name and content as message.


def send_email(addressTo, content):
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

    print("\nSending email as", UserName, "to", addressTo)
    server.sendmail(UserName, addressTo, message)
    print("Email sent successfully")
    server.quit()
    print("Logging out and exiting smtp gmail server")
    time.sleep(1)
    ("Done")


def sendMailInsurance():
    # Checks if file exist

    if os.path.isfile(IOFilePathInsurance):
        # Reads in the template content from file

        with open(
            "/home/martin/projects/mailing_list_insurance/insurance_template.txt", "r"
        ) as template:
            content = template.read()

        # Opens the source file for reading and writing
        with open(IOFilePathInsurance, "r+") as IOFile:
            # Initiates variable for containing the rows of the source file
            lines = []

            reader = csv.reader(IOFile, delimiter=",")

            # Iterates through rows of source file and initiates sending out emails

            for row in reader:
                # Initiates temporary container for current row
                temp = row

                # Checks if the email isn't already sent out to customer
                if row[2] != "Sent":
                    email = row[1]
                    name = row[0]

                    # Sets the current customers name in the text
                    content = content.format(name)

                    send_email(email, content)

                    # Flags current customer
                    temp[2] = "Sent"

                # Appends current row in to lines container
                lines.append(temp)

            IOFile.close()

            # Deletes source file beforehand
            os.remove(IOFilePathInsurance)

        template.close()

        # Creates source file from lines container with updated data

        with open(IOFilePathInsurance, "w", newline="") as newCsvFile:
            writer = csv.writer(newCsvFile, delimiter=",")

            # Write the rows to the source file using writerows().

            writer.writerows(lines)
            newCsvFile.close()


def sendMailCredit():
    # Checks if file exist

    if os.path.isfile(IOFilePathCredit):
        # Reads in the template content from file

        with open(
            "/home/martin/projects/mailing_list_insurance/credit_template.txt", "r"
        ) as template:
            content = template.read()

        # Opens the source file for reading and writing
        with open(IOFilePathCredit, "r+") as IOFile:
            # Initiates variable for containing the rows of the source file
            lines = []

            reader = csv.reader(IOFile, delimiter=",")

            # Iterates through rows of source file and initiates sending out emails

            for row in reader:
                # Initiates temporary container for current row
                temp = row

                # Checks if the email isn't already sent out to customer
                if row[2] != "Sent":
                    email = row[1]
                    name = row[0]

                    # Sets the current customers name in the text
                    content = content.format(name)

                    send_email(email, content)

                    # Flags current customer
                    temp[2] = "Sent"

                # Appends current row in to lines container
                lines.append(temp)

            IOFile.close()

            # Deletes source file beforehand
            os.remove(IOFilePathCredit)

        template.close()

        # Creates source file from lines container with updated data

        with open(IOFilePathCredit, "w", newline="") as newCsvFile:
            writer = csv.writer(newCsvFile, delimiter=",")

            # Write the rows to the source file using writerows().

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
