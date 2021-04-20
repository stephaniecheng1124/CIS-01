# Stephanie Cheng
# CIS 41B Spring 2019
# In-class assignment B
# Problem B1 
#
# This program writes a script to perform various basic math and string operations. 


def string_count():
    name = raw_input("Please enter your name: ")
    print(name.upper())
    print(len(name))
    print(name[3])
    
    name2 = name.replace("o", "x")
    print(name2)
    print(name)
    print("\n")
    
    quote = "Believe you can and you're halfway there."
    
    print("Number of occurrences of letter 'a' in quote:")
    print(quote.count("a"))
    print("\n")
    print("Indices of letter 'a' in quote:")
    
    if quote.count("a") > 0:
        start = quote.find("a")
        print(start)
        
        if quote.count("a") > 1:
            start += 1
            while quote.find("a", start) != -1:
                start = quote.find("a", start)
                print(start)
                start += 1
            
    
string_count()
    
    

