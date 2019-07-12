
##DataTypes
#5 DataTypes

#Number
#String
#List
#Tuple
#Dictionary

#numbers
#there are two types of numbers in python, floating numbers(numbers with a decimal) and interger numbers

intergerNumber = 10
floatingNumber = 20.75

print(floatingNumber)
#prints out 20.75

print(intergerNumber)
#prints out 10

#you can check the DataType of a variable by using the type() method
print (type(floatingNumber))
#prints out <class 'float'>

#you can change the datatype of a variable using Type Casting
floatingNumber = int(floatingNumber)
#this changes the floating number into an interger number

print(type(floatingNumber))
#this prints out <class 'int'>

print(floatingNumber)
#this prints out 20
