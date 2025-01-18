import random
# in Python instead of using console.log() we use print()
#Can still use single or double quotes 
# Indendtion is REALLY important 

print("Hello World!")

#Variables do not need var, const or let. Just name them and then assign the data 
#rememember to capitalise booleans 

my_name = "Lottie"
my_age = 31
a_member = False
#print(a_member)

#to update a variable you just reassign 

a_member = True
#print(a_member)

#Errors

syntax_error = "an error when you've written something wrong, such as mismatched quotes or a missing bracket"

name_error = "trying to print an undefined variable for example"

#Numbers 

an_int = 2 #a whole num
a_float = 10.5 #a decimal point 

# print(an_int + 3)
# print(a_float / 2)

#performing calculations with python (much like performing calculations with any language )

add = 1+1

minus = 2-1

times = 4*4

division = 70/4

modulo = 90 % 7 

exponentiation = 2**3

#concatenation, joining to variables together 

greeting = "hello"
name = "Yoda"

sign_in_text = greeting + ' ' + name

#print(sign_in_text)

#plus equals, for if you have a variable you need to update eg adding another number 

number_of_miles_hiked = 12

number_of_miles_hiked += 2 

#print(number_of_miles_hiked) - prints out 14

#multi line strings 

this_is_one = """
hello
multiple 
lines """

#control flow - how your programme makes decisions. E.G two cards are played, which one is higher, the higher one wins 

#Boolean - True or False (capitalised in Python)

1 == 1 #equals operator (true)

1 != 2 #not equals operator (this will return true)

1 != 1 #this will return False

'7' == 7 #false cos different data types

a_num = 9

print(type(a_num))

#Function 

def just_a_num(num):
  return num

print(just_a_num(3))

def add_one(num):
  return num + 1

#if Statements - conditional statements IF is raining: bring brolly innit 

is_it_raining = False

def bring_brolly():
  brolly_update = ""
  if is_it_raining == True:
    brolly_update = "bring brolly"
  else:
    brolly_update =  "Brolly not needed"
  return brolly_update

#print(bring_brolly())

#AND OR NOT operators

and_operator = "And takes two bollean expressions to evaluate, if both are True it returns True otherwise it returns False "

type = "dog"
name = "Watson"

#if type == "dog" and name == "Watson":
  #print("Wow the goodest of boys")

or_operator = "evaluates if one or another bolean expressions are true, if either are true it returns true"

#if type == "dog" or name == "Watson":
  #print("All dogs are good dogs man! ")

not_operator = "if it's incorrect it returns True, if it's correct it'll return false. E.g not 1+1 == 2 would return False. but not 7 < 0 would return True ~"

type = "cat"
name = "Felix"
#if not type == "dog" and not name == "Watson":
  #print("an interloper!")

#else statements tell the code what to do when conditions are not met and are always found with if statements 

#if type == "dog" or name == "Watson":
  #print("a lovely boy")
#else: 
  #print("mmm sus")

#Elif statements - checks another condition after the first if statement but before the final else statement - you can make as many elif statements as you need in a code block 
type = "dog"
name = "Chewie"
message = ""

if type == "dog" and name == "Watson":
  message = "Lotties Best Friend"
elif type == "dog" and name == "Chewie":
  message = "Lotties other trusted confident"
elif type == "dog":
  message = "mans best friend"
else: 
  message = "hmm sure they're fine"

#print(message)

#MAtch statements - Switch statements in python are called match-case 

#rewriting the above as a switch 

name = "Watson"
message = ""
match name: 
  case "Watson":
    message = "A good boy!"
  case "Chewie":
    message = "Another good guy!"
  case "Scotty":
    message = "Not a dog but humans are good too!"
  case default:
    message = "Who tf is that?"
#print(message)

#Magic eight ball 

name = "Scotty"
question = "Should I clean the kitchen for Lottie?"
answer = ""
#generate a number between one and nine
random_num = random.randint(1,9)
#print(random_num)

match random_num:
  case 1:
    answer = "Yes - definitely"
  case 2:
    answer = "It is decidedly so"
  case 3: 
    answer = "Without a doubt"
  case 4: 
    answer = "Reply hazy, try again"
  case 5: 
    answer = "Ask again later"
  case 6: 
    answer = "Better not tell you now"
  case 7:
    answer = "My sources say no"
  case 8:
    answer = "Outlook not so good"
  case 9:
    answer = "Very doubtful"
  case default:
    answer = "The eight ball spirits are asleep"

#print(f"{name} asks the Magic Eight Ball '{question}'. The magic eight ball replies, {answer}")


















#two sums - neetcode video come back to 

#def two_sums(nums, target):

  