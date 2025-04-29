def over_nine_thousand(lst):
  num = 0
  for int in lst:
      num += int
      if num >= 9000:
         break
  return num
  
print(over_nine_thousand([8000, 900, 120, 5000]))