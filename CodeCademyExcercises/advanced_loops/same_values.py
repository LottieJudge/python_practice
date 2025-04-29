def same_values(lst1, lst2):
  matching = []
  zipped = zip(lst1, lst2)
  for num, num2 in zipped:
    if num == num2:
      matching.append(num)
  return matching

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

