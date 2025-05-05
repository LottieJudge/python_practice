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

def count_all_letters(str):
  number = 0
  for letter in str:
    number += 1
  return number

print(count_all_letters(dog))

# checking if it contains a letter function - although not pythonic 
def letter_check(word, letter):
  for char in word:
    if char == letter:
       return True
  return False

# using in and not in 

def common_letters(str1, str2):
  list = []
  for letter in str1:
    if letter in str2 and letter not in list:
      list.append(letter)
  return list

print(common_letters("Scott Godfrey", "Lottie Judge"))

# lower, upper and title built in methods 

name = "lottIe jUdGe"
name_lower = name.lower()
name_title = name.title()
name_upper = name.upper()

print(name_lower, name_title, name_upper)

# split method takes in an argument and will split the string based on that argument 

sentence = "I love dogs"
sentence_split = sentence.split(' ')
print(sentence_split)

# escape sequences \n - new line \t - horizontal tab

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""
spring_storm_lines = spring_storm_text.split("\n")

print(spring_storm_lines)

# joining strings. the delimiter is where you want the string to join and the arugument is the string it'self - the opposite to split 

my_dogs = ["Watson", "Chewie", "Harry", "Tug", "Ziggy", "Kurgen"]

print(" ".join(my_dogs))

# can also join on a comma to create a CSV

print(",".join(my_dogs))

# using new line as the delimiter 
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = "\n".join(winter_trees_lines)
print(winter_trees_full)

# strip() - removing elements from strings to clean them up, e.g whitespace 

bad_dogs = "    there's no bad dogs     "
print(bad_dogs)
print(bad_dogs.strip(" "))
# strips from either side but not the middle 
# can use anyhthing as the arugument 

bad_humans = "lots of bad humans tho !!!!!!!!"
print(bad_humans.strip("!"))

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []

for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())

print(love_maybe_lines_stripped)

love_maybe_full = "\n".join(love_maybe_lines_stripped)
print(love_maybe_full)

# replace, takes two arguments, replaces all instances string_name.replace(substring_to_replace, new_substring)

toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")
print(toomer_bio_fixed)

# find. takes a string as an argument and searches the string it was run on 

god_wills_it_line_one = "The very earth will disown you"



