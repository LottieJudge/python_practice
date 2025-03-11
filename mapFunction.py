#map functions - map is a built in method, map applies a specificfunction to each item given in the iterable 

# syntax
# map(function, iterable, [iterable2, iterable3])
function = "the function to be applied to each iterable"
iterable = "the iterable the function is to be applied to"

#  so 

def double(num):
  return num * 2

numbers = [1, 2, 3, 4, 5]
doubled_nums = map(double, numbers)

print(list(doubled_nums))

def findRemain(x, y):
  return x % y

numbers=[4, 800, 70, 86, 900]
modulo = 7

map(double, numbers, modulo)