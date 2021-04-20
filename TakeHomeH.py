# Stephanie Cheng
# CIS 41A Spring 2019
# Unit H take-home assignment 
#

# First Script - Variable-Length Keyword Arguments - kwargs

def overseerSystem(**kwargs):
    for k in kwargs.keys():
        if k == "temperature":
            if kwargs[k] > 500:
                print("Warning: temperature is", kwargs[k])
        elif k == "CO2level":
            if kwargs[k] > 0.15:
                print("Warning: CO2level is", kwargs[k])
        elif k == "miscError":
            print("Misc error #", kwargs[k])


# Second Script - Operator Overloading

class BritCoins():
    
    __coinValues = {"penny" : 1, "shilling" : 12, "pound" : 240}    
    
    
    def __init__(self, **kwargs):
        self.totalPennies = 0
        
        for k in kwargs.keys():
            if k == "penny":
                self.totalPennies += kwargs[k]* BritCoins.__coinValues["penny"]
            elif k == "shilling":
                self.totalPennies += kwargs[k]* BritCoins.__coinValues["shilling"]
            elif k == "pound":
                self.totalPennies += kwargs[k]* BritCoins.__coinValues["pound"]

    def __add__(self, other):
        val = self.totalPennies + other.totalPennies
        return BritCoins(penny=val)
    
    def __sub__(self, other):
        val = self.totalPennies - other.totalPennies
        return BritCoins(penny=val) 
    
    def __str__(self):
        total = self.totalPennies
        pound = total//BritCoins.__coinValues["pound"]
        total -= pound * BritCoins.__coinValues["pound"]
        shill = total//BritCoins.__coinValues["shilling"]        
        total -= shill * BritCoins.__coinValues["shilling"]
        penny = total
    
        return str(pound) + " pounds " + str(shill) + " shillings " + str(penny) + " pennies"


def main():
    overseerSystem(temperature=550)
    overseerSystem(temperature=475)
    overseerSystem(temperature=450, miscError=404)
    overseerSystem(CO2level=0.18)
    overseerSystem(CO2level=0.2, miscError=418)
    
    c1 = BritCoins(pound=4, shilling=24, penny=3) 
    c2 = BritCoins(pound=3, shilling=4, penny=5) 
    c3 = c1 + c2
    c4 = c1 - c2
    
    print(c1)
    print(c2)
    print(c3)
    print(c4)
   
main()


''' 
Execution results: 
Warning: temperature is 550
Misc error # 404
Warning: CO2level is 0.18
Warning: CO2level is 0.2
Misc error # 418
5 pounds 4 shillings 3 pennies
3 pounds 4 shillings 5 pennies
8 pounds 8 shillings 8 pennies
1 pounds 19 shillings 10 pennies 
''' 