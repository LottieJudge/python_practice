import re

def LongestWord(sen):
  senList = sen.split(" ")
  senList = [re.sub(r"[^a-zA-Z]","",-) for - in senList]
  longestWord = max(senList)
  print(longestWord)
  print(senList)


print(LongestWord("fun&!! time"))