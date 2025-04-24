def larger_sum(lst1, lst2):
  sum1 = sum(lst1)
  sum2 = sum(lst2)
  if sum1 > sum2:
    return lst1
  elif sum2 > sum1:
    return lst2
  else:
    return lst1
  
print(larger_sum([1, 9, 5], [2, 3, 7]))