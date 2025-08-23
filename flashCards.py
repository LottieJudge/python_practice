NoneKeyword = 'The None Keyword is used as a workaround when defining empty lists/dictionaries as arguments. If you define an empty dataset within a function, every time you call that function it will call all previous iterations. So the None workaround defines the argument as none, which you then redefine as a data set within the function itself.'

def noneKeyWord(age, type=None):
  if type is None:
    type = {}
  print(age, type)

noneKeyWord(4, 'Sweetcorn')