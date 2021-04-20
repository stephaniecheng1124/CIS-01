# Stephanie Cheng
# CIS 41B Spring 2019
# In-class assignment J part 1

import LibraryBook
import LibraryPatron

def main():
    
    b1 = LibraryBook.Book("Alice in Wonderland", "Juvenile")
    b2 = LibraryBook.Book("The Cat in the Hat", "Juvenile")
    b3 = LibraryBook.Book("Harry Potter and the Sorcerer's Stone", "Juvenile")
    b4 = LibraryBook.Book("The Hobbit", "Juvenile")
    b5 = LibraryBook.Book("The Da Vinci Code", "Adult")
    b6 = LibraryBook.Book("The Girl with the Dragon Tattoo", "Adult")
                    
    p1 = LibraryPatron.JuvenilePatron("Jimmy")
    p2 = LibraryPatron.AdultPatron("Sophia")
                
    p1.checkOutBook(b6)
    p1.checkOutBook(b1)
    p1.checkOutBook(b2)
    p1.printCheckedOutBooks()
    p1.checkOutBook(b3)
    p1.returnBook(b1)
    p1.checkOutBook(b3)
    p1.printCheckedOutBooks()
    p2.checkOutBook(b5)
    p2.checkOutBook(b4)
    p2.printCheckedOutBooks()    

main()