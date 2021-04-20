# Stephanie Cheng
# CIS 41A Spring 2019
# Unit C take-home assignment 
#
# Print with monospace font!!!!!!!!!!!!!!

def working_lists():
    list1 = []
    list1.append(1)
    list1.append(3)
    list1.append(5)
    list2 = [1,2,3,4]
    list3 = list1 + list2
    
    print("d) list3 is: " + str(list3))
    print("e) list3 contains a 3: " + str(3 in list3))
    print("f) list3 contains " + str(list3.count(3)) + " 3's")
    print("g) The index of the first 3 contained in list3 is: " + str(list3.index(3)))
    first3 = list3.pop(list3.index(3))
    print("h) first3 = " + str(first3))
    list4 = sorted(list3)
    print("i) list3 is now: " + str(list3))
    print("j) list4 is: " + str(list4))
    print("k) Slice of list3 is: " + str(list3[2:5]))
    print("l)  length of list3 is " + str(len(list3)))
    print("m) The max value of list3 is " + str(max(list3)))
    list3.sort()
    print("n) Sorted list3 is: " + str(list3))
    list5 = [list1, list2]
    print("o) list5 is: " + str(list5))
    print("p) Value 4 from list5 is: " + str((list5[1][3])))
working_lists()

print("\n")

def bits():
    a = 9
    b = 14
    
    print("b) binary of a: " + str(bin(a)))
    print("b) binary of b: " + str(bin(b)))
    print("c) binary of a & b: " + str(bin(a & b)))
    print("d) binary of a | b: " + str(bin(a | b)))

bits()

''' 
Execution results: 
d) list3 is: [1, 3, 5, 1, 2, 3, 4]
e) list3 contains a 3: True
f) list3 contains 2 3's
g) The index of the first 3 contained in list3 is: 1
h) first3 = 3
i) list3 is now: [1, 5, 1, 2, 3, 4]
j) list4 is: [1, 1, 2, 3, 4, 5]
k) Slice of list3 is: [1, 2, 3]
l)  length of list3 is 6
m) The max value of list3 is 5
n) Sorted list3 is: [1, 1, 2, 3, 4, 5]
o) list5 is: [[1, 3, 5], [1, 2, 3, 4]]
p) Value 4 from list5 is: 4


b) binary of a: 0b1001
b) binary of b: 0b1110
c) binary of a & b: 0b1000
d) binary of a | b: 0b1111
''' 