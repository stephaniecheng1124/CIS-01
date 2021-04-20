# Stephanie Cheng
# CIS 41A Spring 2019
# Unit G take-home assignment 
#

# Part One – Reading a data file
import csv

with open('States.txt', 'rt') as fin: 
    cin = csv.DictReader(fin, delimiter = ' ', fieldnames = ['State', 'Region', 'Population'])
    data = [row for row in cin]
    
# print and find state with highest population in the Midwest
highestpop = 0
thestate = "None"

for i in range(len(data)):
    if data[i]['Region'] == "Midwest" and int(data[i]['Population']) > highestpop:
        highestpop = int(data[i]['Population'])
        thestate = data[i]['State']
print('Highest population state in the Midwest is:', thestate, highestpop)


# Part Two – A Dictionary of Lists
with open('USPresidents.txt', 'rt') as fin: 
    cin = csv.DictReader(fin, delimiter = '\t', fieldnames = ['State', 'Name'])
    data = [row for row in cin]
    
dict = {}

for i in range(len(data)):
    key = data[i]['State']
    if key in dict:
        dict[key].append(data[i]['Name'])
    else: 
        listy = [data[i]['Name']]
        dict.update({data[i]['State'] : listy})
    
#print(dict) 
max = 0
thestate = "None"        
for k in dict.keys():
    if len(dict[k]) > max:
        max = len(dict[k])
        thestate = k
        
print("The state with the most presidents is", thestate, "with", max, "presidents:")
for x in dict[thestate]:
    print(x)
 
 

# Part Three – Dictionary Keys and Sets

# Create a dict {State: Num of presidents}
with open('USPresidents.txt', 'rt') as fin: 
    cin = csv.DictReader(fin, delimiter = '\t', fieldnames = ['State', 'Count'])
    data = [row for row in cin]
    
dict2 = {}
for i in range(len(data)):
    key = data[i]['State']
    if key in dict2:
        dict2[key] += 1
    else: 
        dict2.update({data[i]['State'] : 1})
        
        
# Create a dict {State : Population}       
with open('States.txt', 'rt') as fin: 
    cin = csv.DictReader(fin, delimiter = ' ', fieldnames = ['State', 'Region', 'Population'])
    data3 = [row for row in cin]   
    
dict3 = {}
for i in range(len(data3)):
    dict3.update({data3[i]['State'] : int(data3[i]['Population'])})
        
populations = sorted(dict3.values())

# Get the 10 largest populations
topten = populations[-10::]
print(topten)

# Find the states that correspond to the populations and put them into a set
# The set of 10 most populous states:
popstates = set()
for i in range(len(data3)):
    if int(data3[i]['Population']) in topten:
        popstates.add(data3[i]['State'])
print(popstates)

# Set with populous states with presidents born
popwithpres = popstates & set(dict2.keys())

print(len(popwithpres), "out of", len(popstates), "have had presidents born in them:")

for k in sorted(dict2.keys()):
    if k in popwithpres:
        print(k, " ", dict2[k])




''' 
Execution results: 

Highest population state in the Midwest is: IL 12802000
The state with the most presidents is VA with 8 presidents:
George_Washington
James_Madison
James_Monroe
John_Tyler
Thomas_Jefferson
William_Henry_Harrison
Woodrow_Wilson
Zachary_Taylor
[9928000, 10147000, 10310000, 11614000, 12784000, 12802000, 19745000, 20612000, 27863000, 39250000]
{'MI', 'IL', 'GA', 'NC', 'NY', 'FL', 'OH', 'PA', 'TX', 'CA'}
8 out of 10 have had presidents born in them:
CA   1
GA   1
IL   1
NC   2
NY   5
OH   7
PA   1
TX   2
'''