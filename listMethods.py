import math
count = ".count() - a list method to count the number of times an element occurs in a list"
insert = ".insert() - a list method to insert an element at a specified index"
pop = ".pop() - a list method to remove an element at the end of the list or at a specified index"
range_func = ".range() - a built in function to create a sequence of integers"
len_func = "A built in Python function to get the length of a list"
sort_sorted = "A method and function to sort a list"

fave_birds = ["Humble Rock Dove", "Robin", "Osprey", "Hen Harrier"]

#insert
fave_birds.insert(2, "Red Kite")
print(fave_birds)

#removing by index - pop()
fave_birds.insert(3, "Water Vole")
print(fave_birds)
remove_wrong_bird = fave_birds.pop(3)
print(remove_wrong_bird)

#Range - The function range() takes a single input, and generates numbers starting at 0 and ending at the number before the input.So, if we want the numbers from 0 through 9, we use range(10) because 10 is 1 greater than 9:

how_good_are_birds = range(11)
print(list(how_good_are_birds))

#creatuing a range that starts after zero 
how_good_are_birds_really_tho = range(10, 21)
print(list(how_good_are_birds_really_tho))

#or by two (can go up in any increments)
how_good_are_birds_really_tho_by_two = range(2, 21, 2)
print(list(how_good_are_birds_really_tho_by_two))

#length - get the length of a list girly pop 

def length_of_birds(list):
  length = len(list)
  return length;  

print(length_of_birds(fave_birds))

a = 10 
b = 24
print(a +b)

def RecursionChallenge(num):
  num = math.factorial(num)
  # code goes here
  return num

# keep this function call here 
print(RecursionChallenge(8))

def StringChallenge(num):
  str = ""
  if num < 60:
    str = "0:{}".format(num)
  elif num >= 60: 
   num2 = num % 60
   numpre = (num - num2) / 60
   num1 = int(numpre)
   first = "{}:".format(num1)
   second = first + "{}".format(num2)
   str = second

  num = str
  return num


print(StringChallenge(63))
# keep this function call here

def StringChallenge(strParam):
  vowels = ["a", "e", "i", "o", "u", " "]
  consts = []
  for letter in strParam:
    if letter.lower() not in vowels:
      consts.append(letter)
    newStr = "".join(consts)
  strParam = len(newStr)
  # code goes here
  return strParam
print(StringChallenge("Hello World"))


def ArrayChallenge(strArr):
  str1 = strArr[0]
  str2 = strArr[1]
  matches = 0
  for  letter1, letter2 in zip(str1, str2):
    if letter1 != letter2:
      matches += 1
  strArr = matches
  return strArr

print(ArrayChallenge(["10011", "10100"]))

name = "alice"
print(alice)