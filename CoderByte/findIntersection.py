def FindIntersection(strArr):
  wholeString = " ".join(sorted(strArr))
  print(wholeString)
  newString = ""
  for char in set(wholeString):
    if  char.isdigit() and wholeString.count(char) > 1:
      newString += f"{char}, "
      
  return newString
  


# keep this function call here 
print(FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]));