a_list = "a built in data structure to store collections of data. Called an array in JavaScript"
list_example = ["Pigeon", "Crow", "Raven"]

#methods for manipulating the lists 

fave_books = ["Gathering Moss", "Wee Free Men", "English Pastoral", "Rivers of London", "Jamie Oliver fifteen minute meals"]

#adding to the end
def add_book(book):
  fave_books.append(book)

add_book("Sabriel")
print(fave_books)

#adding multiple items
add_more_books = fave_books + ["Silent Spring", "Forgotten Rainforests", "The Night Raven", "Dune"]
print(add_more_books)

#removing book by name
def remove_book(book):
  fave_books.remove(book)

remove_book("Jamie Oliver fifteen minute meals")
print(fave_books)
