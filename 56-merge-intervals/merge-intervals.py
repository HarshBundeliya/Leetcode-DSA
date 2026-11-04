class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        Time Complexity = O(nlogn)
        Space Complexity = O(n)
        
        """
        n = len(intervals)
        intervals.sort()
        result = []
        current = intervals[0]
        for i in range(1,n):
            second = intervals[i]
            if current[1] >= second[0]:
                current = [current[0], max(second[1],current[1])]
            else:
                result.append(current)
                current = intervals[i]
        result.append(current)
        return result