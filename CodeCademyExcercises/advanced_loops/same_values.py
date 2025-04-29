def same_values(lst1, lst2):
  matching = []
  zipped = zip(lst1, lst2)
  # using range and length for to loop through lst 1 and then going through the index in them - v interesting! 
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      matching.append(i)
  return matching

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

