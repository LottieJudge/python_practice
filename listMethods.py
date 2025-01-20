import math
count = ".count() - a list method to count the number of times an element occurs in a list"
insert = ".insert() - a list method to insert an element at a specified index"
pop = ".pop() - a list method to remove an element at the end of the list or at a specified index"
range_func = ".range() - a built in function to create a sequence of integers"
len_func = "A built in Python function to get the length of a list"
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

#Range - The function range() takes a single input, and generates numbers starting at 0 and ending at the number before the input.So, if we want the numbers from 0 through 9, we use range(10) because 10 is 1 greater than 9:

how_good_are_birds = range(11)
print(list(how_good_are_birds))

#creatuing a range that starts after zero 
how_good_are_birds_really_tho = range(10, 21)
print(list(how_good_are_birds_really_tho))

#or by two (can go up in any increments)
how_good_are_birds_really_tho_by_two = range(2, 21, 2)
print(list(how_good_are_birds_really_tho_by_two))

#length - get the length of a list girly pop 

def length_of_birds(list):
  length = len(list)
  return length;  

print(length_of_birds(fave_birds))

#slicing lists - extracting a portion of a list
more_birds = ["Peregrine", "Long-Eared Owl", "Sparrow Hawk"]
fave_birds = fave_birds + more_birds

print(fave_birds)

#selecting the first three
first_three = fave_birds[0:3]
print(first_three)

#keeping the last three
last_three = fave_birds[-3:]
print(last_three)

#yeeting the last three 
slicing_last_three = fave_birds[:-3]
print(slicing_last_three)


def adding_bird(list, word):
  result = [word] * (len(list) * 2 - 1)
#using slice assignment to add in after every second index and then assigning the value to result
  result[0::2] = list
  return result

fave_birds = adding_bird(fave_birds, "pigeon")
print(fave_birds)
 #counting in a list - .count(), count the number of times an element appears 
amount_of_pidge = fave_birds.count("pigeon")
print(amount_of_pidge) 

#sorting lists e.g alphabetical 
fave_birds.sort()
print(fave_birds)

#reverse alphabet
fave_birds.sort(reverse=True)
print(fave_birds)

#sorted() = comes before the list cos built in function and generates a new list 

fave_birds_abc = sorted(fave_birds)
print(fave_birds_abc)

#lens slice activity 


