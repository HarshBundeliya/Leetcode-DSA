class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        # Time Complexity = O(n)
        # Space Complexity = O(1)
        n = len(nums)
        result = 0
        for i in range(n):
            if n % (i+1) == 0:
                result += nums[i]*nums[i]
        return result
