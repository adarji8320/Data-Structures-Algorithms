# Rotate Image by 90 degree counterclockwise

# Problem Statement: Given a matrix, your task is to rotate the matrix 90 degrees counterclockwise.

# https://stackoverflow.com/questions/53250821/in-python-how-do-i-rotate-a-matrix-90-degrees-counterclockwise

class Solution():

    def rotateMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        matrix.reverse()
    
    def printMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j], " ", end='')
            print()

matrix = [
            [1, 2, 3],
            [2, 3, 3],
            [5, 4, 3]
        ]

s1 = Solution()
s1.printMatrix(matrix)
s1.rotateMatrix(matrix)
print("------------")
s1.printMatrix(matrix)