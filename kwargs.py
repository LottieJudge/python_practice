# KWAAAARGS == unlimited KEY WORD ARGUMENTS - not just args, we've got kwargs, two askerisks bb 

tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}
  
def assign_food_items(table_number, **order_items):
# using the get method to assign the keyword argument to a variable to be able to use
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food 
  tables[table_number]['order']['drinks'] = drinks
  print(f'Food: {food}', f'Drinks: {drinks}')

assign_food_items(2, food='burger', drinks='beer')
# move print again for DRY principles 
print(tables) 

