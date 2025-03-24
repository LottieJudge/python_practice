import re

def QuestionsMarks(strParam):
  QM = "?"
  strParam = re.sub(r'/^[A-Z]+$/i', '', strParam)
  print(strParam)

  #  if strParam.count(QM) > 3:


# keep this function call here 
print(QuestionsMarks('aa6?9'))