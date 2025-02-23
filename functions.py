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

def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
  
  print("Here is what your trip will look like!")
  print(f"First, we will stop in{first_destination}, then {second_destination}, and lastly {final_destination}")


trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner(first_destination="Iceland", final_destination="Germany", second_destination="India")
trip_planner("Brooklyn", "Queens")

#built in vs user defined functions 

#built in functions are methods that are already apart of the Python frame work e.g len()

dogs = ["Watson", "Chewie", "Ziggy", "Harry", "Tug", "Kurgen", "Lucky"] 
print(len(dogs))
#the above uses two built in functions - print and len 
dog_age = [6, 4, 12, 5, 6, 4, 1]
max_age = max(dog_age)
min_age = min(dog_age)
print(max_age)
print(min_age)

dog_food_price = 17.89
nicer_price = round(dog_food_price, 1)
print(nicer_price)

#Variable access e.g local, global - if a variable is inside a function the scope of the variable is local, if it's outside of the function it's global 

global_var = "this variable is global"
def function():
  local_var = "this is local"

print(global_var)
#print(local_var) #produces a syntax error! 

#return keyword - returns the output of a function 
def sum(a, b):
  return a + b

print(sum(1,2))

def trip_planner_welcome(name):
  print(f"Welcome to trip planner {name}")

trip_planner_welcome("Lottie")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(3.3)

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print(f"Your trip starts off in {origin}")
  print(f"And you are traveling to {destination}")
  print(f"You will be traveling by {mode_of_transport}")
  print(f"It will take approximately {estimated_time} hours")

destination_setup("London", "Shetland", estimate)

#lambda function - anonymous function
a_b = lambda a, b : a * b
print(a_b(1,2))

#farenheit to celcius 

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  c_temp = round(c_temp, 2)
  return c_temp

f100_in_celcius = f_to_c(100)
print(f100_in_celcius)

#celcius to farenhiet 

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp
c0_in_farenheit = c_to_f(0)
print(c0_in_farenheit)