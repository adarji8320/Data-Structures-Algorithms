# Kadane’s Algorithm : Maximum Subarray Sum in an Array

# Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum and print the subarray.

class Solution:

    def maxSubArraySum(self, arr):

        if len(arr) == 0: return

        sum, maximum = 0, arr[0]

        for x in arr:
            sum += x
            if sum > maximum: maximum = sum
            if sum < 0: sum = 0
                
        return maximum


s1 = Solution()
maximum = s1.maxSubArraySum([-2,1,-3,4,-1,2,1,-5,4])
print(maximum)