# Stephanie Cheng
# CIS 41A Spring 2019
# Unit D take-home assignment 
#

from collections import namedtuple

def sets():
    
    #Part 1: Sets
    class1 = {"Li", "Audry", "Jia", "Migel", "Tanya"}
    class2 = {"Sasha", "Migel", "Tanya", "Hiroto", "Audry"}
    class3 = {"Migel", "Zhang", "Hiroto", "Anita", "Jia"}
    print("Students in all three classes: ", sorted(class1 & class2 & class3))
    print("All students:", sorted(class1 | class2 | class3))
    print("Students in class1 but not class2 or class3:", sorted(class1 - (class2 | class3)))

    #Part 2: Swap
    elements = [1,2,3]
    elements[1], elements[2] = elements[2], elements[1]
    print("List after swap: ", elements)
    
    #Part 3: Tuple Basics - Tuple unpacking
    tup = ("Casablanca", 1942, "romantic drama")
    title, year, genre = tup
    print("The title of my favorite movie is: ", title)
    
    #Part 4: Named Tuple
    Movie = namedtuple('Movie', 'title year genre')
    tup = Movie('Casablanca', 1942, 'romantic drama')
    print("The title of my favorite movie is: ", tup.title)
    
    #Part 5: Named Tuple Containing a List
    Moviestars = namedtuple('Moviestars', 'title year genre stars')
    favoritemovie = Moviestars('Casablanca', 1942, 'romantic drama', ['Humphrey Bogart', 'Ingrid Bergman'])
    favoritemovie.stars.append('Claude Rains')
    print("My favorite star is: ", favoritemovie.stars[1])
    print(favoritemovie)
    
    
sets()

''' 
Execution results: 
Students in all three classes:  ['Migel']
All students: ['Anita', 'Audry', 'Hiroto', 'Jia', 'Li', 'Migel', 'Sasha', 'Tanya', 'Zhang']
Students in class1 but not class2 or class3: ['Li']
List after swap:  [1, 3, 2]
The title of my favorite movie is:  Casablanca
The title of my favorite movie is:  Casablanca
My favorite star is:  Ingrid Bergman
Moviestars(title='Casablanca', year=1942, genre='romantic drama', stars=['Humphrey Bogart', 'Ingrid Bergman', 'Claude Rains'])

''' 