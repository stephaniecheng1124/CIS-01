# Stephanie Cheng
# CIS 41B Spring 2019
# In-class assignment E
# Problem E1 
#

def movies():
    scifi = ['Alien', 'Solaris', 'Inception', 'Moon']
    comedy = ['Borat', 'Idiocracy', 'Superbad', 'Bridesmaids']
    themovie = input("Please enter a movie title: ")
    
    if themovie in scifi:
        print(themovie, "is a scifi movie.")
    elif themovie in comedy:
        print(themovie, "is a comedy movie")    
    else: 
        print("I don't know what genre", themovie, "is.")
        
def looping():
    
    #Using range with a for loop
    for x in range(10, -1, -2):
        print(x)
        
    #Looping through dictionary items
    movies = {
        'The Wizard of Oz' : 193, 
        'The Godfather' : 1972, 
        'Lawrence of Arabia' : 1962, 
        'Raging Bull' : 1980           
    }

    for x in sorted(movies.keys()):
        print(x, "was made in", movies[x])

movies()
movies()
movies()
looping()

  