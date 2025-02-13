"""
Created on
"""
#Libraries
import numpy as np
import re

#Creating the object
class SudokuBrute:
    def __init__(self, toSolve):
        if toSolve is None:
            self.board = np.zeros((9, 9), dtype=int)
        else:
            self.board = toSolve
        #Corresponds to the given position in the 9 x 9 board
        self.row = 0
        self.col = 0
        #Records the number of operations it takes to solve the given puzzle
        self.steps = 0
        #Which section of the sudoku a number is currently in
        self.box = 0
        #

    #
    def solve(self, board):
        pass

    #
    def grid(self, gridNo):
        pass

    #
    def showBoard(self):
        for i in range(9):
            for j in range(9):
                print(self.board[i][j], end=" ")

#Parsing sudoku strings
def Parse_Sudoku(string):
    #Decode characters into integer
    def decode_char(char):
        return int(char) if char.isdigit() else 0

    #Removing useless whitespace
    grid = string.replace('n','')

    decoded = [decode_char(char) for char in grid]

    #Making sure puzzle is correct length
    if len(decoded) != 81:
        raise ValueError("Invalid Sudoku grid")

    #Reshaping to 9 x 9 array
    sudoku_array = np.array(decoded).reshape(9, 9)

    return sudoku_array

#Allowing the user to select the difficulty they want
#def Difficulty_Selector():
    



#Initalizing the object
if __name__ == '__main__':
    easy = SudokuBrute(None)
    medium = SudokuBrute(None)
    hard = SudokuBrute(None)


