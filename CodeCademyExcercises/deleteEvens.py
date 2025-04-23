def delete_starting_evens(my_list):
  while len(my_list) > 0 and my_list[0] % 2 == 0: 
    my_list = my_list[1:0]

  return my_list

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))

while i < 6:
  print(i)
  if i == 3:
    break
  i += 1