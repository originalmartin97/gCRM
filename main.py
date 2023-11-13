from functions import process


# This code only uses csv and txt formatted files as source.

# Sends an email to the specified address with the specified name and content as message.


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
