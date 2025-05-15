with open("/Users/lottiejudge/Desktop/codingFiles/python_practice/CodeCademyExcercises/learningFiles/python.txt") as text_file:
  text_data = text_file.read()

# print(text_data)
with open("/Users/lottiejudge/Desktop/codingFiles/python_practice/CodeCademyExcercises/learningFiles/poem.txt") as poem_file:
  for line in poem_file.readlines():
    print(line)


with open("/Users/lottiejudge/Desktop/codingFiles/python_practice/CodeCademyExcercises/learningFiles/poem.txt") as poem_byLine:
  first_line = poem_byLine.readline()
  second_line = poem_byLine.readline()
  print(second_line)

with open("/Users/lottiejudge/Desktop/codingFiles/python_practice/CodeCademyExcercises/learningFiles/new_poem.txt", "w") as new_poem:
  new_poem.write("I cry on the bank of Blackfriars, filling up old lady Thames to the brim breaking the barrier that fences her in she floods my entire city as the newscaster reads many dead, such a pity x ")

with open("/Users/lottiejudge/Desktop/codingFiles/python_practice/CodeCademyExcercises/learningFiles/new_poem.txt") as new_poem_byLine:
  print(new_poem_byLine.readlines())

with open("/Users/lottiejudge/Desktop/codingFiles/python_practice/CodeCademyExcercises/learningFiles/new_poem.txt", "a") as poem_append: 
  poem_append.write("\n... Causey x ")
  print(poem_append)