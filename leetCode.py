#flowers
#0 = empty and one means not empty, flower cannot be planted next to another flower. if a flower can be planted the function should return true, if not should return false. 
#need a return statmemnet of boolean true or false and 

# true_flowerbed = 1
# false_flowerbed = 1
# flowerbed = [1, 0, 0, 0, 1]

# def canPlaceFlowers(flowerbed, n):
#       count_zero = flowerbed.count(0)
#       count_one = flowerbed.count(1)
#       for index, num in enumerate(flowerbed):
#         if(count_zero > count_one) and (count_zero > n + 1):
#             if(flowerbed[index] == 0):
#               pre = flowerbed[index -1]
#               post = flowerbed[index +1]
#                 if (pre == num) and (post == num):
               
#       else:
#         return False

# counted = canPlaceFlowers([1, 0, 0, 0, 0, 1], 2)
# print(counted)

# def countValidWords(s):
#     # Write your code here
#     a = s.split( )
#     validWords = 0
#     vowel = 'aeiou'
#     cons = 'bcdfghjklmnpqrstvwxyz'
    
#     for word:
#         if len(word) >= 3:
#             v = False
#             c = False
#             for char in word:
#                 if char in vowel:
#                     v = True
#                 elif char in cons:
#                     c = True
#                 if v and c:
#                     validWords += 1 
#                     break
#     print(validWords)
#     return validWords

# countValidWords("This is Form16 submis$ion date")