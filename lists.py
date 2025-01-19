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

#Accessing list elements (by index etc)
#getting list of books with indexing 
def fave_books_by_index(books): 
  for i, book in enumerate(books):
    print(f"{i}:{book}")

print(fave_books_by_index(fave_books))

#getting a specific book by index 
print(fave_books[1])

#negative indexing - last element of the list 
print(fave_books[-1])