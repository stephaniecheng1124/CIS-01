# Stephanie Cheng
# CIS 41B Spring 2019
# In-class assignment D
# Problem D1 
#
def dict_sets():
    
    # Script1
    dict = {
        "apple" : "sauce", 
        "peach" : "cobbler", 
        "carrot" : "cake",
        "strawberry" : "sorbet",
        "banana" : "cream pie"
    }
    
    dict.update({"mango" : "sticky rice"})
    dict["strawberry"] = "shortcake"
    del dict["carrot"]
    print("apple dessert is: " , dict["apple"])
    print("banana dessert exists: " , str("banana" in dict))
    print("pear dessert exists: " , str("pear" in dict))
    print("dict_keys(" , str(dict.keys()) + ")")
    print("dict_values(" , str(dict.values()) + ")")
    print("dict_items(" , str(dict.items()) + ")")
    
    
    
    # Script2
    capitols1 = {
        "Alabama" : "Montgomery", 
        "Alaska" : "Juneau", 
        "Arizona" : "Phoenix", 
        "Arkansas" : "Little Rock", 
        "California" : "Sacramento"         
    }
    
    capitols2 = {
        "California" : "Sac.", 
        "Colorado" : "Denver", 
        "Connecticut" : "Hartford" 
    }

    capitols1.update(capitols2)
    print("Sorted state capitols: " + str(sorted(capitols1.values())))
    
    # Script 3
    class1 = {"Li", "Audry", "Jia", "Migel", "Tanya"}
    class2 = {"Sasha", "Migel", "Tanya", "Hiroto", "Audry"}
    class1.add("John")
    print("Students in both classes: " ,  str(sorted(class1 & class2)))
    print("All students: " ,  str(sorted(class1 | class2)))
    print("Sasha is in class1: " , str("sasha" in class1))
    
    
dict_sets()