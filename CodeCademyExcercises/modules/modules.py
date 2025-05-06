# a module is a collection of python declarations (a library) eg importing random from math 

# date time module
from datetime import datetime 
current_time = datetime.now()
print(current_time)

# random module
import random 
# choice = random.choice("takes a list and returns a random list item")
# number = random.randint("takes an argument of two numbers and returns a number in that range. e.g a dice")
# using list comprehension to create the list 
random_list = [random.randint(1,100) for i in range(101)]
randomer_number = random.choice(random_list)
print(randomer_number)