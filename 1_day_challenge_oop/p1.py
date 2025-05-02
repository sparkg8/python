# Create a Book class that includes attributes like title, author, and year. Add a method to display the details.
# Create a Lybrary class that contains a collection of books
# and add some methods, remove_book, add_book, and display_books.
# Create a Book class
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_details(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"
    
book1 = Book("The power of words", "Mariano Sigman", 2022)

print(book1.display_details())