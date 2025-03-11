# lambda is a built in function that can have any number of arguments but only one expression, its anonymous so you don;t have to define the function and is used for quick operations. because it only has one expression the arguements are evaludated and returned immediately 

# syntax 

# lambda arguments: expression

add = lambda a, b: a + b 

print(add(3, 5))

greeting = lambda name: f"Hello {name}!"

print(greeting("Lottie"))

# you can use the lambda function in conjunction with higer order functions such as map 
