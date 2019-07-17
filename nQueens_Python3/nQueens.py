#first we will print the matrix

print("Enter num: ")

num = int(input())

for row in range(1, num):#iterates through rows in matrix
  for column in range(1, num):#iterates through the columns the matrix
    print(0, end = " ")#prints the num and ends with a space after every print statement
  print()#this empty print function will print the num dymanically after every column loop is executed
