# Set Matrix Zero - Solution 1

# Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.

class SolutionOne:

    def setZeroes(self, matrix):

        # Return if matrix is empty
        if len(matrix) == 0 or len(matrix[0]) == 0: return

        row = [False] * len(matrix)
        column = [False] * max(map(len, matrix))

        # Store the rows and columns positions being zero.
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row[i] = True
                    column[j] = True

        # Set value zero to the qualified row(s) and column(s).
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if row[i] == True or column[j] == True:
                    matrix[i][j] = 0


    def printMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j], " ", end='')
            print()


matrix = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
]

s2 = SolutionOne()
s2.printMatrix(matrix)
s2.setZeroes(matrix)
print("------------------------")
s2.printMatrix(matrix)
