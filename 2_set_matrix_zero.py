# Set Matrix Zero - Solution 2

# Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.

class SolutionTwo:

    def setZeroes(self, matrix):

        # Return if matrix is empty
        if len(matrix) == 0 or len(matrix[0]) == 0: return

        zero_positions = []
        
        # Store the rows and columns positions being zero.
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if( matrix[i][j] == 0):
                    zero_positions.append((i, j))
        
        # Set value zero to the qualified row(s) and column(s).
        for z in zero_positions:
            x, y = z
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if( i == x or j == y):
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

s2 = SolutionTwo()
s2.printMatrix(matrix)
s2.setZeroes(matrix)
print("------------------------")
s2.printMatrix(matrix)
