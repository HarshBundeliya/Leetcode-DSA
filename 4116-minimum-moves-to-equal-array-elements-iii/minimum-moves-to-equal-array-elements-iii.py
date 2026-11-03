class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        Time Complexity = O(n)
        Space Complexity = O(1)
        """
        target = max(nums)
        result = sum( target-num for num in nums)
        return result