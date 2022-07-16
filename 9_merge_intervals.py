# Merge Overlapping Sub-intervals

# Problem Statement: Given an array of intervals, merge all the overlapping intervals and return an array of non-overlapping intervals.

class Solution:

    def mergeIntervals(self, intervals):

        if len(intervals) == 0 or len(intervals) == 1: return intervals
        
        intervals.sort()
        mergedInterval = []

        start, end = intervals[0][0], intervals[0][1]
        
        for i in intervals:
            if i[0] <= end:
                end = max(end, i[1])
            else:
                mergedInterval.append([start, end])
                start, end = i[0], i[1]
                
        mergedInterval.append([start, end])
        return mergedInterval
            

intervals = [
        [1, 3],
        [2, 6],
        [15, 18],
        [8, 10]
    ]

s1 = Solution()
results = s1.mergeIntervals(intervals)
print (results)