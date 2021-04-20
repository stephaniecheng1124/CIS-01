# Stephanie Cheng
# CIS 41A Spring 2019
# Unit J take-home assignment 
#

# Part 1 of 1 - Part 1 of 1 – Nested Loop Dice Game

import random

def playgame():
    earnings = 0
    thenum = random.randrange(1,7)  

    while thenum != 1 and thenum != 2 and thenum != 3:
        earnings += thenum
        thenum = random.randrange(1,7) 
    return earnings    
        


largest = 0
allearnings = 0

for x in range(1, 10001):
    earn = playgame()
    allearnings += earn
    if earn > largest:
        largest = earn

print("Average amount won:", round(allearnings/10000, 2))    
print("Max amount won:", largest)

''' 
Execution results: 
Average amount won: 5.04
Max amount won: 62 
''' 