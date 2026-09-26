class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Time Complexity = O(n)
        # Space Complexity = O(1)
        res = 0
        for num in nums:
            res ^= num 
        return res

        