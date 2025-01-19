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

#reassigning index values 
print(fave_books[1])
fave_books[1] = "How to be a woman"
print(fave_books[1])

#2D Lists - a list within a list 

fave_book_with_rating = [["Gathering Moss", 5], ["Wee Free Men", 5], ["Silent Spring", 5]]

#Accessing 2D Lists 
#accessing the sublist at 1 and then the name of that book which will be at 0 
second_book = fave_book_with_rating[1][0]
print(second_book)

last_book = fave_book_with_rating[-1][-1]
print(last_book)