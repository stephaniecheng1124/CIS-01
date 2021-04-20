# Stephanie Cheng
# CIS 41A Spring 2019
# Unit B take-home assignment 
# Problem B1



# Script 1: Working  with strings

def working_with_strings():
    something = raw_input("Please enter a string: ")
    print(something.isupper())
    print(something.isdigit())
    print(something.isalpha())
    
    haiku = "Type, type, type away. \nCompile. Run. \nHip hip hooray! \nNo error today!"
    print(haiku)
    
    quote = "And now for something completely different"
    print(quote[:6])
    print(quote[-4:])
    print(quote[14:16])
    print(quote[::2])
    print(quote[::-1])
    
    pattern1 = ".~*'"
    pattern2 = pattern1 + pattern1[::-1]
    for i in range(5): 
        print(pattern2),  
    
    print("\n")
        
        
# Script 2: Formatting

def invoice():
    SMALL = 9.20
    MEDIUM = 8.52
    LARGE = 7.98
    
    smallOrder = int(input("How many boxes of small beads would you like: "))
    mediumOrder = int(input("How many boxes of medium beads would you like: "))
    largeOrder = int(input("How many boxes of large beads would you like: "))
    
    print('{0:<8s} {1:>5s} {2:>15s} {3:>10s}'.format("SIZE","QTY", "COST PER BOX", "TOTALS"))
    print('{0:<8s} {1:>5d} {2:>15.2f} {3:>10.2f}'.format("Small",smallOrder, SMALL, smallOrder * SMALL))
    print('{0:<8s} {1:>5d} {2:>15.2f} {3:>10.2f}'.format("Medium",mediumOrder, MEDIUM, mediumOrder * MEDIUM))
    print('{0:<8s} {1:>5d} {2:>15.2f} {3:>10.2f}'.format("Large",largeOrder, LARGE, largeOrder *LARGE))
    print('{0:<8s} {1:>32.2f}'.format("TOTAL", smallOrder * SMALL + mediumOrder * MEDIUM + largeOrder *LARGE))
    
working_with_strings()
invoice()
invoice()

    
''' 
Execution results: 
Please enter a string:ABC123
True
False
False
Type, type, type away. 
Compile. Run. 
Hip hip hooray! 
No error today!
And no
rent
me
Adnwf
tnere
.~*''*~. .~*''*~. .~*''*~. .~*''*~. .~*''*~. 

How many boxes of small beads would you like: 10
How many boxes of medium beads would you like: 9
How many boxes of large beads would you like: 8
SIZE       QTY    COST PER BOX     TOTALS
Small       10            9.20      92.00
Medium       9            8.52      76.68
Large        8            7.98      63.84
TOTAL                              232.52
How many boxes of small beads would you like: 5
How many boxes of medium beads would you like: 10
How many boxes of large beads would you like: 15
SIZE       QTY    COST PER BOX     TOTALS
Small        5            9.20      46.00
Medium      10            8.52      85.20
Large       15            7.98     119.70
TOTAL                              250.90
''' 