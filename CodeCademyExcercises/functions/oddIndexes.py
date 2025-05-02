def odd_indices(my_list):
  odd_list = []
  for i, num in enumerate(my_list):
    if i % 2 != 0:
      odd_list.append(num)
  return odd_list

print(odd_indices([4, 3, 7, 10, 11, -2]))    
  