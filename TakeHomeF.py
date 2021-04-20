# Stephanie Cheng
# CIS 41A Spring 2019
# Unit F take-home assignment 
#

# Part One – Keyword Arguments and Default Values
def invoice(unitPrice, quantity, shipping = 10, handling = 5):
    print("Cost (unitPrice x quantity) = ", unitPrice * quantity)
    print("Shipping = ", shipping)
    print("Handling = ", handling)
    print("Total = ", unitPrice * quantity + shipping + handling)

# Part Two – args (Variable-Length Arguments)
def printGroupMembers(groupname, *args):
    print("Members of", groupname)
    for x in range(0,len(args)):
        print(args[x]) 


# Part Three – Non-Rectangular (Ragged) 2D lists  
def buildBell(numRows):
    listoflist = [[1]]
    
    for r in range(1, numRows):
        aRow = []
        for c in range(r + 1):
            if c == 0:
                aRow.append(listoflist[r-1][-1])
            else:
                num = listoflist[r-1][c-1] + aRow[c-1]
                aRow.append(num)
            
        listoflist.append(aRow)
        
    return listoflist

def printBell(listy):
    for x in range(len(listy)):
        for y in range(x + 1):
            if x != y:
                print("{0:>6}".format(listy[x][y]), end = ' ')
            else:
                print("{0:>6}".format(listy[x][y]))
            

def main():
    invoice(20, 4, shipping = 8)
    invoice(15, 3, handling = 15)
    printGroupMembers("Group A", "Li", "Audry", "Jia") 
    groupB = ["Sasha", "Migel", "Tanya", "Hiroto"] 
    printGroupMembers("Group B", *groupB)
    listy = buildBell(8)
    printBell(listy)

main()
    
    
''' 
Execution results: 
Cost (unitPrice x quantity) =  80
Shipping =  8
Handling =  5
Total =  93
Cost (unitPrice x quantity) =  45
Shipping =  10
Handling =  15
Total =  70
Members of Group A
Li
Audry
Jia
Members of Group B
Sasha
Migel
Tanya
Hiroto
     1
     1      2
     2      3      5
     5      7     10     15
    15     20     27     37     52
    52     67     87    114    151    203
   203    255    322    409    523    674    877
   877   1080   1335   1657   2066   2589   3263   4140
 
''' 