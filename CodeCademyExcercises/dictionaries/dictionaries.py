# a dictionary is an unordered set of key: value pairs (key = key : value = the data lads) its a way of mapping data so that we can find values quickly that are associated to one another e.g 

menu = {"Latte":3, "Flat White": 3.5, "Tea": 1.5, "Filter": 1}
print(menu)

# dictionaries can be any data type - even more dictionaries!!! 
books_i_like = {"Nature":["The Golden Mole", "English Pastorial", "Britains Rainforests"], "Fantasy":["Wee Free Men", "Rivers of London", "Villager"]}
print(books_i_like)

# invalid keys - e.g a list as a key - just wont cut it 

# adding a key/new item
books_i_like["SciFi"] = "Dune"
print(books_i_like)

#method for adding various key:value pairs .update()
books_i_like.update({"Biography":"Down the Drain", "Fiction - cosy": "Thursday Murder Club", "SelfHelp":"How to Quit Smoking"})
print(books_i_like)

# Overwriting values - using the key you can overwrite it 
books_i_like["Biography"] = "Strong Female Character"
print(books_i_like["Biography"])

# Dict comprehensions (combining dictionaries)
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
full_menu = {key:value for key, value in zip(drinks,caffeine)}
print(full_menu)

# getting a key and accessing the keys in the dictionary- its indexing 
print(full_menu["decaf"])

# get() method to get a key instead, if the key doesn't exist it returns none 

full_menu.get("tea") #will return none instead of an error 
# or you can provide a default value and it will add it 
full_menu.get("tea", 30)

# deleting a key using pop()
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)

# getting all keys 
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()
print(users)
print(lessons)

# get all values, using values() accesses the value in the key value pair, meaning you could add everything 
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0 
for x in num_exercises.values():
  total_exercises += x
print(total_exercises)

# get all items, get the key and the value with items()

for genre, value in books_i_like.items():
  print(f"{genre} has a value of {value}")

# codecademy second go 

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
for title, value in pct_women_in_occupation.items():
  print(f"Women make up {value} percent of {title}s.")

  # end of module exercise 

tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}
spread = {}
spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for key, value in spread.items():
  print(f"Your {key} is the {value} card.")