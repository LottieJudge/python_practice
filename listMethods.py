
count = ".count() - a list method to count the number of times an element occurs in a list"
insert = ".insert() - a list method to insert an element at a specified index"
pop = ".pop() - a list method to remove an element at the end of the list or at a specified index"
range = ".range() - a built in function to create a sequence of integers"
len = "A built in Python function to get the length of a list"
sort_sorted = "A method and function to sort a list"

fave_birds = ["Humble Rock Dove", "Robin", "Osprey", "Hen Harrier"]

#insert
fave_birds.insert(2, "Red Kite")
print(fave_birds)

#removing by index - pop()
fave_birds.insert(3, "Water Vole")
print(fave_birds)
remove_wrong_bird = fave_birds.pop(3)
print(remove_wrong_bird)

