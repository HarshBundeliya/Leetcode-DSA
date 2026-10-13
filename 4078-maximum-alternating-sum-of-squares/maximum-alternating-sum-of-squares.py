class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Time Complexity = O(nlog(n))
        # Space Complexity = O(1)

        n = len(nums)
        nums.sort(key=abs)

        result = 0
        for i, num in enumerate(nums):
            if i < n//2:
                result -= num*num
            else:
                result += num*num
        return result