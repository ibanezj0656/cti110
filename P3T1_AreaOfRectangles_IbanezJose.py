#This program will determine which area of a rectangle is larger
#March 5, 2020
#CTI-110 P3T1 - Areas of Rectangles
#Jose Ibanez
#

print("Welcome, please enter whole numbers for this program")

#Length and width of the first rectangle
rectOneLength = int(input("What is the length of the first rectangle? "))
rectOneWidth = int(input("What is the width of the first rectangle? "))

#Length and width of the second rectangle
rectTwoLength = int(input("What is the length of the second rectangle? "))
rectTwoWidth = int(input("What is the width of the second rectangle? "))

#Find the areas of both rectangles
rectOneArea = rectOneLength * rectOneWidth
rectTwoArea = rectTwoLength * rectTwoWidth

#Compare the areas
if rectOneArea > rectTwoArea:
    print("Rectangle One's area is greater than Rectangle Two.") #One is greater than two
elif rectOneArea < rectTwoArea:
    print("Rectangle Two's area is greater than Rectangle One.") #Two is greater than one
else:
    print("The areas of both rectangles are equal.") #Rectangles are equal in area
