"""
Created on
"""
#Libraries
import numpy as np

#Creating the object
class SudokuBrute:
    def __init__(self, toSolve):
        if toSolve is None:
            self.board = np.zeros((9, 9), dtype=int)
        else:
            self.board = toSolve
        self.row = 0
        self.col = 0
        self.steps = 0
        self.box = 0

    def solve(self, board):
        pass

    def grid(self, gridNo):
        pass

    def showBoard(self):
        for i in range(9):
            for j in range(9):
                print(self.board[i][j], end=" ")

#Initalizing the object
if __name__ == '__main__':
    easy = SudokuBrute(None)
    medium = SudokuBrute(None)
    hard = SudokuBrute(None)


