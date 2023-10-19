import csv
import smtplib
import os
import time

user_name = "metlife.martin@gmail.com"
user_password = "qboxnhnoquehleyw"
io_file_path_insurance = (
    "/home/martin/projects/mailing_list_insurance/potential_customers_insurance.csv"
)
io_file_path_credit = (
    "/home/martin/projects/mailing_list_insurance/potential_customers_credit.csv"
)
io_file_path_pension = (
    "/home/martin/projects/mailing_list_insurance/potential_customers_pension.csv"
)
template_text_path_insurance = (
    "/home/martin/projects/mailing_list_insurance/insurance_template.txt"
)
template_text_path_credit = (
    "/home/martin/projects/mailing_list_insurance/credit_template.txt"
)
template_text_path_pension = (
    "/home/martin/projects/mailing_list_insurance/pension_template.txt"
)

# This code only uses csv and txt formatted files as source.

# Sends an email to the specified address with the specified name and content as message.


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
    # Sleep for one second - avoiding losing connection and errors with SMTP
    time.sleep(1)
    ("Done")


def process(category):
    if category == "1":
        template_text = template_text_path_insurance
        io_file = io_file_path_insurance
    elif category == "2":
        template_text = template_text_path_credit
        io_file = io_file_path_credit
    elif category == "3":
        template_text = template_text_path_pension
        io_file = io_file_path_pension
    else:
        print("Category is not valid")

    with open(template_text, "r") as template:
        template_content = template.read()

    if os.path.isfile(io_file):
        with open(io_file, "r+") as source_file:
            lines = []
            reader = csv.reader(source_file, delimiter=",")

            for row in reader:
                if "Értesítve: email" not in row[6] and "NEM" not in row[6]:
                    address = row[5]
                    name = row[0]
                    content = template_content.format(name)

                    send_email(address, content)

                    row[6] = "Értesítve: email"

                lines.append(row)

        source_file.close()
        template.close()
        os.remove(io_file)

        with open(io_file, "w", newline="") as new_csv_file:
            writer = csv.writer(new_csv_file, delimiter=",")

            # Write the rows to the source file using writerows()
            writer.writerows(lines)
            new_csv_file.close()

        lines = []
    else:
        print("There isn't any new potential customer file.")


if __name__ == "__main__":
    print("Martin Marketing Mailing System")

    while True:
        user_input = input(
            "\n\n\nWhat do you want to do?\n\n0 - Exit program\n1 - Send out emails about insurance to potential customers\n2 - Send out emails about credit to potential customers\n3 - Send out emails about pension to potential customers\n"
        )

        if user_input == "1":
            process(user_input)
        elif user_input == "2":
            process(user_input)
        elif user_input == "3":
            process(user_input)
        elif user_input == "0":
            print("\n\nGoodbye! :)")
            break
