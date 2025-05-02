# take in two lists and return the lists combined and sorted 

def combine_sort(my_list1, my_list2):
  newList = my_list1 + my_list2
  return sorted(newList)


print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))