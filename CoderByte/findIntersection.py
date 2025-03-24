def FindIntersection(strArr):
  strArr = (", ").join(strArr)
  strArr =  strArr.split(",")
  print(strArr)
  nums = []
  for num in set(strArr):
      if strArr.count(num) > 1:
       nums.append(num)
      #  print(nums)

  
# keep this function call here 
print(FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]));

