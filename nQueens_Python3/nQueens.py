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
        if target_row == self.size:#once target row equals the size of the board the function will stop running
            self.show_full_board(positions)#and will display the solution
            self.solutions += 1#the solutions variable will increase by 1 every time a solutions is found
        else:
            for column in range(self.size):#iterates through the positions list
                if self.check_place(positions, target_row, column):#calls the check_place function for every position of the board
                    positions[target_row] = column#when the if condition in check_place function return false, the column will have the same value as the target row
                    self.put_queen(positions, target_row + 1)#after every iteration of check_place function, target_row will increment by 1 and put_queen function will run again

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

    def check_place(self, positions, ocuppied_rows, column):
        for i in range(ocuppied_rows):
            if positions[i] == column or \
                positions[i] - i == column - ocuppied_rows or \
                positions[i] + i == column + ocuppied_rows:
#the above block of code checks if the placement of a queen at a given position is a valid option by
#the fist statements checks for rook moves
#the second and third statement checks for bishop moves(diagonal lines, one with a positive slope and the other with a negative slope)

                return False#if false, that means at the current position, the queen can be attacked and therefor a possible solution would be null
        return True#if true add 1 to the target_row variable(this means move to the next position (to the right of the board))*and run the self_check_place position again for the new position of i

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




print("Enter num: ")

qNum = int(input())

def main(qNum):
    """Initialize and solve the n queens puzzle"""
    NQueens(qNum)

if __name__ == "__main__":
    # execute only if run as a script
    main(qNum)

input("Press any key to exit")
