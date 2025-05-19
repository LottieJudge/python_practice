import csv 
import json

compromised_users = []

with open("CodeCademyExcercises/hackingTheFender/passwords.csv") as password_file:
  password_csv = csv.DictReader(password_file)
  for line in password_csv:
    password_row = []
    password_row.append(line)
    compromised_users.append(password_row[0]['Username'])

with open('compromised_users.txt', "w") as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(f"Username:{user}.\n ")

with open('boss-message.json', "w") as boss_message:
  boss_message_dict = {
    "recipient" : "The Boss",
    "message" : "Mission Success"
  }