def win_percentage(wins, losses):
  total = wins + losses 
  ratio =  wins / total
  percentage = ratio * 100
  return f"{percentage}%"

print(win_percentage(10, 0))
