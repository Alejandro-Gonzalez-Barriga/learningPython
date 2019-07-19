class NQueens:#we define a class to build different matrix representation fo each of the possible solution

    def __init__(self, size):#the constructor takes the parameter of size to calculate the different solutions depending on the size of the board the user decides to input
        self.size = size#the size of the board
        self.solutions = 0#the counter for each solution found
        self.solve()#this method solves for solutions depending on the size of the board

    def solve(self):
        positions = [-1] * self.size#creates a list (called positions) the size of the input given by the user. Each index will have a starting vale of -1, this will be a one dimensional list where the index number equals the position of the row where the the queen will be placed and the value will equal to the positin in the cloumn where the queen will be placed
        #positions can will be pushed into a solutions list and be stored in the database for future reference
        self.put_queen(positions, 0)#calls the put_queen function with the (positions) list and 0 index as parameter

        print("Found", self.solutions, "solutions.") #this line will print a string stating the total number of solutions found


    def put_queen(self, positions, target_row):

    def show_full_board(self, positions):
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")#this line prints a new line to separate each matrix




print("Enter size of board: ")#prompts the user to enter a board size

qNum = int(input())# assigns user input to num variable, also type casts the input

#script to execute all code in this file
def main(qNum):
    NQueens(qNum)


if __name__ == "__main__":
    main(qNum)
