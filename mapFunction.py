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

# lambda and Map 
squared = map(lambda x: x ** 2, numbers)
sq_list = list(map(lambda x: x ** 2, numbers))

print(squared)
print(sq_list)