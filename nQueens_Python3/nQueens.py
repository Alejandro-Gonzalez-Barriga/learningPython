class NQueens:#we define a class to build different matrix representation fo each of the possible solution

    def __init__(self, size):#the constructor takes the parameter of size to calculate the different solutions depending on the size of the board the user decides to input
        self.size = size#the size of the board
        self.solutions = 0#the counter for each solution found
        self.solve()#this method solves for solutions depending on the size of the board
        



print("Enter num: ")

num = int(input())

for row in range(1, num):#iterates through rows in matrix
  for column in range(1, num):#iterates through the columns the matrix
    print(0, end = " ")#prints the num and ends with a space after every print statement
  print()#this empty print function will print the num dymanically after every column loop is executed
