class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        # Time Complexity = O(n^2)
        # Space Complexity = O(n)
        n = len(nums)
        result = 0
        for i in range(n):
            s = set()
            for j in range(i,n):
                s.add(nums[j])
                result += (len(s))**2
        return result