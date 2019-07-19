class NQueens:#we define a class to build different matrix representation fo each of the possible solution

    def __init__(self, size):#the constructor takes the parameter of size to calculate the different solutions depending on the size of the board the user decides to input
        self.size = size#the size of the board
        self.solutions = 0#the counter for each solution found
        self.solve()#this method solves for solutions depending on the size of the board

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
