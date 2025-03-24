import re

def QuestionsMarks(strParam):
  QM = "?"
  newParam = re.sub(r'[A-Za-z]', '', strParam)
  print(newParam)

  #  if strParam.count(QM) > 3:


# keep this function call here 
print(QuestionsMarks('aa6?9'))