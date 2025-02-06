#we're learning functions! 
def this_is_a_function(num):
  return num * 2

print(this_is_a_function(4))

def more_complicated(num):
  if num < 10:
    return num
  if num > 10:
    num = num * 10
  return num 

print(more_complicated(8))

print("Let's check the weather!")

def weather_check(weather):
  check = weather.lower()
  if check == "sunny":
     print("Pack the factor 50 babe!")
  elif check == "rainy":
    print("Pack the brolly babe!")
  elif check == "windy":
    print("It's a blowin babe!")
  elif check == "snowy":
    print("pack the snow boots babe!")
  else: 
    print("Is weather even real?")

weather_check("flab")

#parameters and aruguments
def my_function(parameter):
  cat = parameter + " and the cat"
  print(f"You can assign values to the parameter of a function. {cat}")

my_function("Watsy")

#more perams 

def a_function(param1, param2):
  if param1 == param2:



