# Stephanie Cheng
# CIS 41A Spring 2019
# Unit E take-home assignment 
#
import random

def decision():
    name = input("Please enter the plant name: ")
    plant = input("Please enter the plant type: ")
    height = int(input("Please enter the plant name: "))
    
    
    if plant == "Vegetable": 
        print("A", name, "can be planted in the Vegetable Garden.")
    elif plant == "Flower":
        if height <= 3: 
            print("A", name, "can be planted in the Low garden or the High Garden.")
        elif height <= 6:
            print("A", name, "can be planted in the High Garden")
        else: 
            print("A", name, "can not be planted in any of these Gardens.")
    else: 
        print("A", name, "can not be planted in any of these Gardens.")
        
def guessing():
    #this generates a random int from 1-100, inclusive
    secretNum = random.randint(1,100)   
    guessed = False
    count = 0
    print("Welcome to the guessing game.")
    print("You need to guess a number from 1 to 100.")
    
    while guessed == False:
        theguess = int(input("Please enter your guess: "))
        count += 1
        if theguess < secretNum:
            print("Your guess is too low!")
        elif theguess >secretNum:
            print("Your guess is too high!")
        else: 
            guessed = True
            print("Your guess is Correct! Congratulations!")
            print("You guessed the secret number in", count, "guesses!")
        

def looping():
    
    #Part one: Looping with string methods
    quote = "Believe you can and you're halfway there."

    print("Indices of letter 'a' in quote:")
    
    if quote.count("a") > 0:
        start = quote.find("a")
        print(start)
        
        if quote.count("a") > 1:
            start += 1
            while quote.find("a", start) != -1:
                start = quote.find("a", start)
                print("a found at index", start)
                start += 1    
    
    #Part two: Nested loops
    rows = int(input("Please enter the number of rows for the multiplication table: ")) 
    
    for r in range (1, rows + 1):
        for c in range (1, r + 1):
            print('{0:>3d}'.format(r * c), end = " ")
           
        print()    
            
for i in range(6):
    decision()
guessing()
looping()
            
        
    
''' 
Execution results: 
Please enter the plant name: Lily
Please enter the plant type: Flower
Please enter the plant name: 3
A Lily can be planted in the Low garden or the High Garden.
Please enter the plant name: Bonsai
Please enter the plant type: Tree
Please enter the plant name: 2
A Bonsai can not be planted in any of these Gardens.
Please enter the plant name: Carrots
Please enter the plant type: Vegetable
Please enter the plant name: 1
A Carrots can be planted in the Vegetable Garden.
Please enter the plant name: Corn
Please enter the plant type: Vegetable
Please enter the plant name: 8
A Corn can be planted in the Vegetable Garden.
Please enter the plant name: Rose
Please enter the plant type: Flower
Please enter the plant name: 5
A Rose can be planted in the High Garden
Please enter the plant name: Sunflower
Please enter the plant type: Flower
Please enter the plant name: 8
A Sunflower can not be planted in any of these Gardens.
Welcome to the guessing game.
You need to guess a number from 1 to 100.
Please enter your guess: 50
Your guess is too high!
Please enter your guess: 30
Your guess is too low!
Please enter your guess: 40
Your guess is too high!
Please enter your guess: 35
Your guess is too high!
Please enter your guess: 32
Your guess is Correct! Congratulations!
You guessed the secret number in 5 guesses!
Indices of letter 'a' in quote:
13
a found at index 16
a found at index 28
a found at index 32
Please enter the number of rows for the multiplication table: 12
  1 
  2   4 
  3   6   9 
  4   8  12  16 
  5  10  15  20  25 
  6  12  18  24  30  36 
  7  14  21  28  35  42  49 
  8  16  24  32  40  48  56  64 
  9  18  27  36  45  54  63  72  81 
 10  20  30  40  50  60  70  80  90 100 
 11  22  33  44  55  66  77  88  99 110 121 
 12  24  36  48  60  72  84  96 108 120 132 144 

''' 
