##Exeption Handeling
#ex. dividng a number by 0. Since that is an invalid operation, that raises an exeption,

#print(10/0)
#prints ArithmeticError

try:
  length = 10
  width = 0
  length /width
except Exception:
  print("Division by 0 is invalid, kindly change your imput")
#prits Division by 0 is invalid, kindly change your imput

#if we devide one of the variables it also raises an exception
del(width)

#print(width)
#prints NameError

try:
  length/width
except NameError:
  print("variable was not defined")
#prints variable was not defined
