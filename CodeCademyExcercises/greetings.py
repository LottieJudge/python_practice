def add_greetings(names):
  greeting_list = []
  for name in names: 
    greeting_list.append(f"Hello, {name}")


print(add_greetings(["Owen", "Max", "Sophie"]))