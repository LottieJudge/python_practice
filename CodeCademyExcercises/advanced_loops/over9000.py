def over_nine_thousand(lst):
  num = 0
  for int in lst:
     while num <= 9000:
      num += int
  return num
  
print(over_nine_thousand([8000, 900, 120, 5000]))