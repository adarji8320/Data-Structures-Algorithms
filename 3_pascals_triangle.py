# Program to generate Pascal’s Triangle

# Problem Statement: Given an integer N, return the first N rows of Pascal’s triangle.

class Solution:

    def generatePascalsTriangle(n):
        
        results = []

        for i in range(1, n+1):
            # first element is always 1
            C = 1
            tmp = []
            for j in range(1, i+1):
                tmp.append(C)
                # using Binomial Coefficient
                C = C * (i - j) // j
            
            results.append(tmp)

        return results

    def printPascalsTriangle(results):
        for i in range(len(results)):
            print(' ' * len(results[len(results)-i-1]) ,end='')
            for j in results[i]:
                print(j, ' ', sep='', end='')
            print()


results = Solution.generatePascalsTriangle(10)
Solution.printPascalsTriangle(results)