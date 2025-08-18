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

def assign_food_items(**order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  print(order_items)


# move print again for DRY principles 
print(tables)



