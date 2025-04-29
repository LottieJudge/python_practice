def reversed_list(lst1, lst2):
  # using slicing instead of reverse ! reverse reruns none which is interesting so should use slicing to return
  reversed = lst1[::-1]
  if reversed == lst2:
    return True 
  else:
    return False 

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))