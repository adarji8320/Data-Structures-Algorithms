# Merge two Sorted Arrays Without Extra Space - Solution One

# Problem statement: Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. Merge them in sorted order. Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.

class SolutionOne:

    def merge(self, arr1, arr2):
        return sorted(arr1 + arr2)[:len(arr1)], sorted(arr1 + arr2)[len(arr1):(len(arr1) + len(arr2))]


arr1 = [1, 4, 8, 10]
arr2 = [2, 3, 9]

print(" :: Before Merge :: ")
print(arr1)
print(arr2)

s1 = SolutionOne()
arr1, arr2 = s1.merge(arr1, arr2)

print(" :: After Merge :: ")
print(arr1)
print(arr2)