def over_nine_thousand(lst):
  num = 0 
  while num <= 9000:
    for int in lst:
      num += int
  return num
  
print(over_nine_thousand([8000, 900, 120, 5000]))