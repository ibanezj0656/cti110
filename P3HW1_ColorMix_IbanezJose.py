#CTI-110
#P3HW1 - Color Mixer
#Jose Ibanez
#March 5, 2020
#


#Pseudocode
#Ask user to input two primary colors
#check to see if the colors are valid
#If the colors are valid, create the new color from the entered colors
#Display the resulting color


#Welcome message and get input from user
print("Welcome to Color Mixer, enter a color in all lowercase letters.")
colorOne = input("What is the first color. ")
colorTwo = input("Whats is the second color. ")

#First color Red
if colorOne == "red":
    if colorTwo == "yellow":
        print("The result is orange.")
    elif colorTwo == "blue":
        print("The result is purple.")
    elif colorOne == colorTwo: 
        print("The colors are the same.") #Same colors
    else:
        print("Enter a valid primary color!") #Type or not a primary color

#First color Blue
if colorOne == "blue":
    if colorTwo == "yellow":
        print("The result is green.")
    elif colorTwo == "red":
        print("The result is purple.")
    elif colorOne == colorTwo:
        print("The colors are the same.") #Same colors
    else:
        print("Enter a valid primary color!") #Type or not a primary color

#First color Yellow
if colorOne == "yellow":
    if colorTwo == "red":
        print("The result is orange.")
    elif colorTwo == "blue":
        print("The result is green.")
    elif colorOne == colorTwo:
        print("The colors are the same.") #Same colors
    else:
        print("Enter a valid primary color!") #Type or not a primary color
