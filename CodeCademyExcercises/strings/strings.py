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

# len - finding the length to the string 
print(len(dog)) #prints six 
# you can use len with indexing to get the last letter of string 
print(dog[len(dog)-1]) 
#was going to be like whats more pythonic but I assume most pythonic would be making it a reusable function?
# negative indexing - access the end much quicker than using len 
print(dog[-1])
# negative indexing slicing - last three 
print(dog[-3:])

# escape characters - enabling use of pythonic charcters such as " " in a string 
best_dog = "Watsons owner Lottie said \"Watson is for sure the best dog!\""

print(best_dog)

# iterating through strings 
best_dogs = "Watson and Chewie"
def print_all_letters(str):
  for letter in str:
    print(letter)

print_all_letters(dog)   