import re

def LongestWord(sen):
  senList = sen.split(" ")
  senList = [re.sub(r"[^a-zA-Z]","",_) for _ in senList]
  longestWord = max(senList, key=len)
  return longestWord
  print(senList)


print(LongestWord("fun&!! time"))