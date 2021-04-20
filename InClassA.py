# Stephanie Cheng
# CIS 41A Spring 2019
# In-class assignment A
# Problem A1
#
# This program creates a height and width for a rectangle. 
# Print the height, width, and area of the rectangle in the following format, with the columns aligned:
# height: x.x
# width:  x.x
# area:   x.xxxxxxx...

def print_info(height, width):
        print("height: " + str(height))
        print("width:  " + str(width))
        print("area:   " + str(height * width) + "\n")
        
        smallheight = height//2
        smallwidth = width//2
        
        print("Smaller Rectangle:")
        print("height: " + str(smallheight))
        print("width:  " + str(smallwidth))
        print("area:   " + str(smallheight * smallwidth))        
        
print_info(7.1, 2.9)




        
