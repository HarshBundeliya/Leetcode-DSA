class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Time Complexity = O(nlog(n))
        # Space Complexity = O(n)

        n = len(nums)
        nums.sort(key=abs)
        odd_position_nums = nums[:n//2]
        even_position_nums = nums[n//2:]

        output = 0
        for even in even_position_nums:
            output +=  even*even
        for odd in odd_position_nums:
            output -=  odd*odd

        return output