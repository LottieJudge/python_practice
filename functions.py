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
  output = ""
  if param1 == param2:
    output = "The same!"
  if param1 != param2:
    output = "oh, different!"
  print(output)

a_function(1,1)

a = [1, 2, 3]
b = [1, 2, 3]
def function(x,y):
  x.append(4)
  y = y + [4]

function(a,b)

#cost calculator - plabe tickets x amount of pople, cost of room, two to a room, so if passenger number over 2 double etc, then times  by night then add all together 

def new_york_cost(plane_ticket, passenger_number, hotel_price, days):
  plane_total = plane_ticket * passenger_number
  hotel_total = 0
  if passenger_number <= 2:
    hotel_total = hotel_price * days 
  if passenger_number > 2: 
    hotel_total = hotel_price * passenger_number / 2 * days 
  trip_total = plane_total + hotel_total
  return trip_total

cost = new_york_cost(400, 2, 50, 5)

print(cost)

#Types of arguments 

positional_argument = "an argument that can be called by their position in the function definition"
keyword_argument = "arguments that can be called by their name"
default_argument = "arguments that are given default values"

def trip_planner(first_destination, second_destination, final_destination):
  final_destination = "Codecademy HQ"