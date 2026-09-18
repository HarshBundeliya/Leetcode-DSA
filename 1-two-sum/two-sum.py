class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Time Complexity = O(n)
        # Space Complexity = O(n)
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            else:
                seen[num] = i
