# Stephanie Cheng
# CIS 41A Spring 2019
# Unit A take-home assignment 
# Problem A1
#
# This program writes a script to perform various basic math and string operations. 

import math

def maths():
    
    
    #Basic math and string operations
    a = 3**2.5
    b = 2
    b += 3
    c = 12
    c /= 4
    d = 5 % 3
    
    print(a)
    print(b)
    print(c)
    print(d)
    print("\n")
    
    #Built-in functions abs, round, and min
    print(abs(5-7))
    print(round(3.14159, 4))
    print(round(186282, -2))
    print(min(6,-9,-3,0))
    print("\n")
    
    #Functions from the math module
    number = input("Please enter number: ")
    print("Square root of your number to two decimal places: " + str(round(math.sqrt(number), 2)))
    print("Log base 10 of your number to two decimal places: " + str(round(math.log10(number), 2)))
    
    #Complex numbers
    z1 = 4 + 3j
    z2 = 2 + 2j
    z3 = z1 * z2
    print(z3)
    
    
    
maths()

''' 
Execution results: 
15.5884572681
5
3
2


2
3.1416
186200.0
-9


Please enter number: 7.6
Square root of your number to two decimal places: 2.76
Log base 10 of your number to two decimal places: 0.88
(2+14j)


''' 


