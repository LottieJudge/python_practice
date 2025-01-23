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

