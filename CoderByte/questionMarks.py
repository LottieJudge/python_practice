import re

def QuestionsMarks(strParam):
  QM = "?"
  newParam = re.sub(r'[A-Za-z]', '', strParam)
  print(newParam)
  for i, question in enumerate(newParam):
     if strParam.count(QM) < 3:
        print(False)


# keep this function call here 
print(QuestionsMarks('aa6?9'))