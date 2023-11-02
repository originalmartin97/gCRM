import json

with open("gmail_credentials.json") as data_file:
    data = json.load(data_file)

user_name = data["username"]
user_password = data["password"]
