# Sort an array of 0s, 1s and 2s

# Problem Statement: Given an array consisting of only 0s, 1s and 2s. Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)

class Solution():

    def threeWayPartition(self, arr):
        
        low = mid = 0
        high = len(arr) - 1

        while mid <= high:

            match arr[mid]:
                case 0:
                    arr[low], arr[mid] = arr[mid], arr[low]
                    low, mid = low + 1, mid + 1
                case 1:
                    mid += 1
                case 2:
                    arr[mid], arr[high] = arr[high], arr[mid]
                    high -= 1
                

arr = [0, 1, 1, 0, 2, 1, 0, 2, 1, 0]
s1 = Solution()
s1.threeWayPartition(arr)
print(arr)