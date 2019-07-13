#this program will determine if a number if a number of both
#3 and 7

#we will be using the % operator to determine if that number has a
#remainder when devided by 3 and then we will do the sasme if that
#number has a remainder when devided by 7

print("enter a number: ")
#the above line will prompt the user to enter a number

num = int(input())
#since you cannot perform an arethmetic operation with a string number
#to take care of that we used Type Casting in order to use the
#string number iputed by the user and convert it to a interger

if num % 3 is 0:
  print("Number is a multiple of 3")
  if num % 7 is 0:
    print("Number is a multiple of 7")
  else:
    print("Number is a multiple of 3, but not of 7") 
