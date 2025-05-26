# Type - to check the type of data stored in a variable etc we use type()

my_string = 'Watson and Chewie are the best!'
my_number = 69
my_dict = {}

print(type(my_string))
print(type(my_number))
print(type(my_dict))

# a class is a template for a data type. it describes the info it will hold and how we can interact with it as engineers - capitalise the name of classes to make them easier to identify from variables. 

class BabysFirstClass:
  pass

# Classes must be instantiated to become alive, we must create an instance of it in order for it to become the schematic


first_class = BabysFirstClass()

# OOP - a class is also an object, defining classes and creating objects to represent the responsibilities is known as OOP. Instanciation takes a class and turns into an object and type() does the opposite, taking an objet and returning a class 

baby_type = type(first_class)
print(baby_type)

# class variables - same data avilable to every instance of a, class, include it in the body of the class 

class BestDog: 
  name = "Watson"

# methods are functions defined within the class. the first argument in a method is always the object that is calling the method. Convention says to anme this argument self, they always need at least one argument. 

class BullDog: 
  dog_time_dilation = 8

  def bulldog_to_human(self):
    print(f'Bulldogs experience {self.dog_time_dilation} years for every one human year!')

watson_dog = BullDog()
watson_dog.bulldog_to_human()

# codecademy practice 
class Rules:
  def washing_brushes():
    return "Point bristles towards the basin while washing your brushes."
  
# methods with arguments, adding more than one argument. EG to make a sum or do something with the data 

class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile

converter = DistanceConverter() #initiating 
three_point_one = converter.how_many_kms(3.1)
print(three_point_one)

# codecademy practice - arguments within class functions

class Circle:
  pi = 3.14
  def area(self, radius):
    return Circle.pi * radius ** 2

# creating an instance 
circle = Circle()
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)

print(pizza_area)

# constructors - dunder methods e.g __init__ - this means the method is called every time an instance is made of a Class 

class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print(f"New circle with diameter: {diameter}")

teaching_table = Circle(36)
   
# instance variables -The data held by an object is referred to as an instance variable. Instance variables aren’t shared by all instances of a class — they are variables that are specific to the object they are attached to.

class Dogs:
  pass

watson = Dogs()
chewie = Dogs()

watson.name = 'Watson'
chewie.name = 'Chewie'

names = "My dogs are called {} and {}".format(watson.name, chewie.name)
print(names)

# attribute functions - if we try to access an attribute (class instance or variable eg) will throw an error but to check if something has an attribute we can use hasattr() method to return true or false or getattr() to return the attribute 

# hasattr(object, “attribute”) has two parameters:
# object : the object we are testing to see if it has a certain attribute
# attribute : name of attribute we want to see if it exists

# getattr(object, “attribute”, default) has three parameters (one of which is optional):
# object : the object whose attribute we want to evaluate
# attribute : name of attribute we want to evaluate
# default : the value that is returned if the attribute does not exist (note: this parameter is optional)

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")

# self - adding in a self identfiying part of the function 

class NewCircle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2
  def circumference(self):
    return 2 * self.pi * self.radius

medium_pizza = NewCircle(12)
teaching_table = NewCircle(36)
round_room = NewCircle(11460)

print(medium_pizza.circumference(), teaching_table.circumference(), round_room.circumference())

# everythings an object! dir() will return an objects attrributes at runtime, Python automatically adds a number of attributes to all objects that get created. These internal attributes are usually indicated by double-underscores.

# print(dir(5))

def this_function_is_an_object(name):
  name = 'Lottie'

# print(dir(this_function_is_an_object))

# string representation - when printing a class it prints that weird line wihtout much info e.g <__main__.Employee object at 0x104e88390>. To return it as string we can use the dunder method __repr__(). this tells python what we want the string rep of the class to be. Only has one peram and returns a string 

class Employee():
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name

argus = Employee("Argus Filch")
print(argus)

# string representation so you can just call the variable immediately 

class RepCircle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius

  def __repr__(self):
    return "A circle with radius {radius}".format(radius = self.radius)
  
  
medium_pizza = RepCircle(12)
teaching_table = RepCircle(36)
round_room = RepCircle(11460)

print(medium_pizza, teaching_table, round_room)