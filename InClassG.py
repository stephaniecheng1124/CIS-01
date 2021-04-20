# Stephanie Cheng
# CIS 41B Spring 2019
# In-class assignment G
# Problem G1 
#

# Part One – Working with Files


firstLine = 'Beautiful is better than ugly.\n'
secondLine = 'Explicit is better than implicit.\n'
theFile = open('ZenOfPython.txt', 'w')
theFile.write(firstLine)
theFile.write(secondLine)
theFile.close()

theFile = open('ZenOfPython.txt', 'a')
seventh = 'Readability counts.\n'
seventeenth = 'If the implementation is hard to explain, it\'s a bad idea.\n'
theFile.write(seventh)
theFile.write(seventeenth)
theFile.close()

theFile = open('ZenOfPython.txt', 'r')
content = theFile.read()
print(content)
theFile.close()


# Part Two – CSV Files
import csv

dict = {}

with open('Cities.csv', 'r') as fin:
    cin = csv.DictReader(fin)
    data = [row for row in cin]
    
   
for i in range(len(data)):
    tup = (data[i]['City'], data[i]['State'])
    dict.update({tup : data[i]['Population']})
    
for k, v in dict.items(): 
    print(k[0], k[1], v)


city = input("Please enter a city:")
state = input("Please enter a state:")

for k, v in dict.items(): 
    if k[0] == city and k[1] == state:
        print(k[0], k[1], "has a population of", v)


