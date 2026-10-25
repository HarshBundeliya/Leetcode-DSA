class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """
        Time Complexity = O(n)
        Space Complexity = O(1)
        """
        n = len(nums)
        expected_sum = n*(n+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum