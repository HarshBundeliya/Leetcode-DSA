class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Time Complexity = O(logn)
        Space Complexity = O(1)
        """
        n = len(nums)
        left = 0
        right = n-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid 
        return nums[left]