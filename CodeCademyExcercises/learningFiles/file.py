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