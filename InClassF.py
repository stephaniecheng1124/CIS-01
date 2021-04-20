# Stephanie Cheng
# CIS 41B Spring 2019
# In-class assignment F
# Problem F 
#


# Part One – Using a main function, Docstrings
def hello():    
   '''
    This function prints the text "Hello World"
   '''
   print("Hello World")
   
   


# Part Two – Error Handling
def printListElement(listy, listindex):
   
   try:
      print(listy[listindex])
   except: 
      print("Error! Bad index number!")
   
# Part Three – How Python function arguments are treated
def byVal(x):
   print("Original ID of parameter in byVal is: ", id(x))
   x += 7
   print("ID of parameter in byVal after change is: ", id(x))

def byRef(listy):
   print("Original ID of parameter in byRef is: ", id(listy))
   print("Original ID of parameter's last element in byRef is: ", id(listy[-1]))
   listy[-1] += 7
   print("ID of parameter in byRef after change is: ", id(listy))   
   print("ID of parameter's last element in byRef after change is: ", id(listy[-1]))   
   
def main(): 
   hello()
   help(hello)
   myList = [0,1,2]
   printListElement(myList, 3)
   myInt = 3
   print("Original ID of myInt in main is: ", id(myInt))
   print("Original ID of myList in main is: ",id(myList))
   print("Original ID of myList's last element in main is: ",id(myList[-1]))
   byVal(myInt)
   byRef(myList)
   print("ID of myInt in main after call to byVal is: ", id(myInt))
   print("ID of myList in main after call to byRef is: ",id(myList))
   print("ID of myList's last element after call to byRef in main is: ",id(myList[-1]))   
   print("myInt is now: ", myInt)
   print("myList is now: ", myList)
   

   
main()