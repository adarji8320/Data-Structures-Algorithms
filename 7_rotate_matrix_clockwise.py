# Rotate Image by 90 degree clockwise

# Problem Statement: Given a matrix, your task is to rotate the matrix 90 degrees clockwise.

class Solution():

    def rotateMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            matrix[i].reverse()
    
    def printMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j], " ", end='')
            print()

matrix = [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
        ]

s1 = Solution()
s1.printMatrix(matrix)
s1.rotateMatrix(matrix)
print("------------")
s1.printMatrix(matrix)