# indexing in strings 
dog = "Watson"
print(dog[0]) #prints W
# slicing string string[firstIndex:lastIndex] - Wat 
print(dog[0:3])
# tson
print(dog[2:])

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  first_splice = first_name[0:3]
  last_splice = last_name[0:3]
  account_name = f"{first_splice}{last_splice}"
  return account_name

