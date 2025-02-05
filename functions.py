#we're learning functions! 
def this_is_a_function(num):
  return num * 2

print(this_is_a_function(4))

def more_complicated(num):
  if num < 10:
    return num
  if num > 10:
    num = num * 10
  return num 

print(more_complicated(8))