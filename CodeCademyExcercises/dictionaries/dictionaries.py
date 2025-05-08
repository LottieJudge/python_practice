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



