#-------------------------------------------------
# Session 1 Assignment 3
# Accept first name and last name and print
# them in reverse
#-------------------------------------------------

#Accept first name and last name
name=input("Enter your name as FirstName LastName:")

#Split the input string to capture first name and last name
firstname,secondname=name.split(" ")

#Print the originlly entered string
print("You have entered %s %s" %(firstname,secondname))

#Print the string in reverse
print("Printing in Reverse - %s %s" %(secondname,firstname))