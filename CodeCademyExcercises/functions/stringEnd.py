def username_generator(first_name, last_name):
  first = first_name[0:3]
  last = last_name[0:4]
  user_name = f"{first}{last}"
  return user_name

print(username_generator("Lottie", "Judge"))

user_name = username_generator("Lottie", "Judge")
def password_generator(user_name):
    last_letter = user_name[-1]
    password = f"{last_letter}{user_name[0:-1]}"
    return password

print(password_generator(user_name))