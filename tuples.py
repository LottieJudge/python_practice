#tuples are immutable meaning they can't be changed but they are more energy efficient in both time and memory (and money baby) - good to use if working with data that doesn't ever need to be changed. A tuple is defined by a variable and then normal brackets (). Tuples can also hold just one item as long as it's followed by a comma 

popcorn_flavours = ("Sweet", "Salty", "Cinnamon", "Butter")

#indexing works the same as lists 
print(popcorn_flavours[0])

#slicing
pop = popcorn_flavours[0:2]
print(pop)

#built in function 

len_tuple = ("The length of the tuple",)
max_tuple = ("Returns the maximum value of the tuple, whatevers closer to z if it's a string and the highest value if numbers", )
min_tuple = ("the same as above but opposite",)
index_tuple = ("bring back the index of an element", )
print(popcorn_flavours.index("Cinnamon"))
count_tuple = ("Counts the number of instances of an element")