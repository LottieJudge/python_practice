#functions from assessments etc 
import math
#figure out the factorial
def RecursionChallenge(num):
  num = math.factorial(num)
  return num

print(RecursionChallenge(8))

#couldn't use f string because the assessment was an older python 
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


#remove vowels and return number of consts
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


#find the amount of elements in two strings[i] that don't match each other 
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