# Stephanie Cheng
# CIS 41B Spring 2019
# In-class assignment C
# Problem C1 
#
#List Script

from copy import deepcopy

def list_script(): 
    list1 = [2, 4.1, 'Hello']
    list2 = list1
    list3 = deepcopy(list1)
    
    print("list1 == list2: " + str(list1==list2))
    print("list1 == list3: " + str(list1==list3))
    print("list2 == list3: " + str(list2==list3))
    
    print("list1 is list2: " + str(list1 is list2))
    print("list1 is list3: " + str(list1 is list3))
    print("list2 is list3: " + str(list2 is list3))
    
    print("list1 ID: " + str(id(list1)))
    print("list2 ID: " + str(id(list2)))
    print("list3 ID: " + str(id(list3)))
    
    list1.append(8)
    list2.insert(1, 'goodbye')
    del list3[0]
    
    print("list1 printed: " + str(list1))
    print("list2 printed: " + str(list2))
    print("list3 printed: " + str(list3))

list_script()
