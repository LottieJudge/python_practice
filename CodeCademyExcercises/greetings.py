def add_greetings(names):
  count = names.count
  for name in names: 
    greeting = f"Hello, {name}"
  return greeting

print(add_greetings(["Owen", "Max", "Sophie"]))