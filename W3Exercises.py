# Pyhton Basics Exercise 1 
# \n brings the code onto a new line and \t indents the string 
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

# Python Basics Exercise 2 
# Prints the python version and info with some print statements to make the info more readable
import sys 
print("Python Version")
print(sys.version)
print("Version info.")
print(sys.version_info)

# Python Basics Exercise 3 
import datetime 
now = datetime.datetime.now()
print("The current date and time is: ")
print( now.strftime("%Y-%M-%D %H:%M:%S"))

# ython basics Exercise 4
from math import pi 
radius =  float(input("Please enter the radius of the circle: "))
print("The area of a circle with the radius " + str(radius) + " is: " +str(pi * radius**2))

# Python Basics Exercise 5
firstn = str(input("Please input your first name: "))
lastn = str(input("Please input your last name: "))
print( "Hello " + lastn + " " + firstn)

# Python Basics Exercise 6
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

# Python Basics Exercise 7 
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))

# Python Basics Exercise 8
color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))

# Python Basics Exercise 9
examDate = (11, 12, 2014)
print("The exam will start from: %i/%i/%i " %examDate)

# Python Basics Exercise 10 
# %s is used to concatenate strings together. Is a palceholder for a string
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)
