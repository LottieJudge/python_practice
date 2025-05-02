#append the sum of the last two elements of the list, After doing so, it repeats this process two more times and returns the resulting list.

def append_sum(list):
  for i in range(3):
    last_two = list[-2:]
    sum_list = sum(last_two)
    list.append(sum_list)
  return list

print(append_sum([1, 1, 2]))
