import csv 

compromised_users = []

with open("passwords.csv") as password_file:
  password_csv = csv.DictReader(password_file)
  for line in password_csv:
    password_row = []
    password_row.append(line)
    compromised_users.append(password_row[0]['Username'])

