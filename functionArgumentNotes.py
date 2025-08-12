positionalArguments = 'Arguments that are called by their position in the function definition'

def printname(firstName, lastName):
  print(firstName, lastName)

printname('Scott', 'Godfrey')

keyWordArgument = 'Arguments that are called by their name, so within the function call assigning them data a bit like you would with a variable'

def printdog(name, age):
  print(name, age)

printdog(name = 'Watson', age = 8)

tables = {
  1: ['Jiho', False],
  2:[],
  3:[],
  4:[],
  5:[],
  6:[],
  7:[],
}

def assign_table(table_number, name, vip_status):
  tables[table_number] = [name, vip_status]

# using positional aruguments in this 
assign_table(9, 'Scott', True)

# using keyword aruguments to assign in this 
assign_table(table_number = 3, name = 'Kay', vip_status= True)


# moved print statement below all for DRY - don't repeat yourself 
print(tables)