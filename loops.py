#Loops are used for repeating tasks in code. E.G looping through a playlist on spotify, or given a specific pin and email looping through customer database to find the matches and returning that info 

playlist = ["English Rose", "Drop Seven", "Worms"]
for song in playlist:
  print(f"now playing {song}")

#without a loop we would have to print the above using indexing - long lads, long! 

print(playlist[0])
print(playlist[1])
print(playlist[2])

#blue print of a loop 

#for temporary_variable in data_structure:
  #print(perform_action)

#the temp variable is i in JS, but can be called anything, it's just used as an instance to iterate through. The Data structure could be a list, dictionary or tuple. and then perform a function. EG append(), pop() or just return it baby 

#loops using range - performing the function a set numbe rof times 

six_times = range(6)

for num in range(6):
  print("Loop number:" + str(num +1))

#while loops - perform a set of instructions as long as the given condition is true 

count = 0

while count <= 10:
  print(count)
  count +=1
print("the big ten!")

#will count to ten!

#as an elegant loop counting down
nums = 3
while count >0: print(count); count -= 1 

shopping_list = ["Oat Milk", "Dog Treats", "Popcorn", "Vichi Catalan"]

list = len(shopping_list)
index = 0 

while index < list:
  print(shopping_list[index])
  index +=1

#will print the shopping list 

am_the_album = ["Do I wanna Know", "R U Mine", "One for the Road", "Arabella", "I want it all", "No.1 party anthem", "Mad Sounds", "Fireside", "Why'd you only call me", "Snap Out Of It", "Knee Socks", "I Wanna be Yours"]

setlist = len(am_the_album)

print("AM Setlist:")
while index < setlist:
  print(am_the_album[index])
  index += 1

  #the dreaded infinite loooooops, if you don't add a stopping clause a loop will run forever and break your code. Avoid(using break helps)

#break 
items_on_sale = ["Neat shirt", "Posh Socks", "Spotty Scarf", "Stylish Eye patch", "Fetching Cane", "Elegant Cummerbund", "Lovely bowtie"]

items_on_sale.sort()

print("Checking we have your wares:")

for item in items_on_sale:
  print(item)
  if item == "Posh Socks":
    break
print("Item acquired!")

#continue = can be used if you need to skip an action or number etc

numbers = [-1, -2, -3, 0, 1, 2, 3]

print("Positive integers only")
for num in numbers:
  if num < 0:
    continue
  print(num)


#Nested Loops 
project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

#printing individual students from the list 
for team in project_teams:
  for student in team:
    print(student)

#without the nesting 
for team in project_teams:
  print(team)
  #prints the individual team as a list