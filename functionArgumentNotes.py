positionalArguments = 'Arguments that are called by their position in the function definition'

def printname(firstName, lastName):
  print(firstName, lastName)

printname('Scott', 'Godfrey')

keyWordArgument = 'Arguments that are called by their name, so within the function call assigning them data a bit like you would with a variable'

def printdog(name, age):
  print(name, age)

printdog(name = 'Watson', age = 8)

defaultAruguments = 'Arguments that are assigned default values, they can be changed but if they are not, they\'ll always render as the default value assigned in the function arugment'

def printMum(name='Sally', age=64):
  print(name,age)

printMum()
printMum('Lisa', 60)


tables = {
  1: ['Jiho', False],
  2:[],
  3:[],
  4:[],
  5:[],
  6:[],
  7:[],
}

# adding in a default value for vip_status
def assign_table(table_number, name, vip_status=False):
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = ''

# using positional aruguments in this 
assign_table(9, 'Scott', True)

# using keyword aruguments to assign in this 
assign_table(table_number = 3, name = 'Kay', vip_status= True)

# using the False default value 
assign_table(4, 'Karla')

# moved print statement below all for DRY - don't repeat yourself 
print(tables)

# variable number of arguments - how does a function now to process as many arguments as it is given without explicitly stating it? e.g the print() function, will just print as many as we pass it, to do this with a function we create we can use the unpacking operator within the function definition * e.g 
# this is actually packing args, unpacking is smushing them all toegther such as a list or tuple 

# packing below : 

def makeItRain(*args):
  print(args)

makeItRain('yes', 'no', 'it', 'is', 'raining', 'args', False, 'or', True, 18)

# args could be any word such as when using i in a for loop 

def noRainNoGain(*weathers):
  print(weathers)

noRainNoGain('Sun', 'Snow', 'Typhoon')

def print_orders_new(*print_orders):
  print(print_orders)

print_orders_new('Oj', 'Apple Juice', 'Seasick Sausage Sandwich')

# unpacking 

shops = ['Boots', 'Argos', 'Oliver Bonas']

# prints as a list 
print(shops)
# prints as string 
print(*shops) 

# another packing function 

def assign_and_print_orders(table_number, *order_items):
  
