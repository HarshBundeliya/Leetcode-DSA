class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i, num in enumerate(nums):
            res[i] = prefix
            prefix *= num

        suffix = 1
        for j in range(n-1,-1,-1):
            res[j] *= suffix
            suffix *= nums[j]

        return res