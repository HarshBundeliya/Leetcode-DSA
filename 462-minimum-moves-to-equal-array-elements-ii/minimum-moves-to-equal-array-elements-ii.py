class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        """
        Time Complexity = O(nlog(n))
        Space Complexity = O(1)
        """
        nums.sort()
        n = len(nums)
    
        median = nums[n//2]

        result = 0
        for num in nums:
            result += abs(num - median)
        return result