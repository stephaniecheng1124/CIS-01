# Stephanie Cheng
# CIS 41B Spring 2019
# In-class assignment J part 3

import LibraryBook

class LibraryPatron():
    def __init__(self, name):
        self.name = name
        self.booksCheckedOut = []
    
    def checkOutBook(self, checkOutLimit, book):      
        if len(self.booksCheckedOut) == checkOutLimit:
            print("Sorry", self.name, "you are at your checkout limit of", checkOutLimit, "books")
        else:
            self.booksCheckedOut.append(book)
            print(self.name, "has checked out", book.title)
    
    
    def returnBook(self, book):
        self.booksCheckedOut.remove(book)
        print(self.name, "has returned", str(book.title))
    
    def printCheckedOutBooks(self):
        if len(self.booksCheckedOut) == 0:
            print(self.name, "has 0 books checked out")
        else: 
            print(self.name, "has the following books checked out:")
            for x in self.booksCheckedOut:
                print(x.title)
                
class AdultPatron(LibraryPatron):
    def __init__(self, name):
        super().__init__(name)
        self.checkOutLimit = 4
        
    def checkOutBook(self, book):
        super().checkOutBook(self.checkOutLimit, book)
        
class JuvenilePatron(LibraryPatron):
    def __init__(self, name):
        super().__init__(name)
        self.checkOutLimit = 2   
        
    def checkOutBook(self, book):
        if book.bookType != "Juvenile":
            print("Sorry", self.name, book.title, "is an adult book")
        else:
            super().checkOutBook(self.checkOutLimit, book)    