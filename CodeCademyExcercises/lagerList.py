# Write a function named larger_list() that has two parameters named my_list1 and my_list2. The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of my_list1.

def larger_list(my_list1, my_list2):
    list1len = len(my_list1)
    list2len = len(my_list2)
    if list1len == list2len:
        return my_list1[-1]
    if list1len > list2len:
        return my_list1[-1]
    else:
        return my_list2[-1]
    
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))