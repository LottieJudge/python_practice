import re

def LongestWord(sen):
  senList = sen.split(" ")
  for word in senList:
    wordNoChars = re.sub(r"[^a-zA-Z]"," ", word)
    newList = senList.append(wordNoChars)
          
print(LongestWord("fun&!! time"))