import csv
import smtplib
import os
import time
import schedule

UserName = "originalmartin97@gmail.com"
UserPassword = "zklybkojdcacniof"
IOFilePath = (
    "/home/martin/projects/mailing_list_insurance/potential_customers_insurance.csv"
)


# This code only uses csv and txt formatted files as source.


# Sends an email to the specified address with the specified name and content as message.


def send_email(addressTo, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(UserName, UserPassword)

    message = "Subject: MetLife Zrt. (Győr)\n\n"
    message += content
    message = message.encode("utf-8")

    server.sendmail(UserName, addressTo, message)
    server.quit()
    time.sleep(1)


def process():
    # Checks if file exist

    if os.path.isfile(IOFilePath):
        # Reads in the template content from file

        with open(
            "/home/martin/projects/mailing_list_insurance/insurance_template.txt", "r"
        ) as template:
            content = template.read()

        # Opens the source file for reading and writing
        with open(IOFilePath, "r+") as IOFile:
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
            os.remove(IOFilePath)

        template.close()

        # Creates source file from lines container with updated data

        with open(IOFilePath, "w", newline="") as newCsvFile:
            writer = csv.writer(newCsvFile, delimiter=",")

            # Write the rows to the source file using writerows().

            writer.writerows(lines)
            newCsvFile.close()


process()
