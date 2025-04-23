
def divisible_by_ten(nums):
  answer = 0
  for num in nums:
    if num % 10 == 0:
      answer += 1
  return answer

print(divisible_by_ten([20, 25, 30, 35, 40]))
