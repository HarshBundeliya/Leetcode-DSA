class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        """
        Time Complexity = O(logn)
        Space Complexity = O(1)
        """
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left+right)//2
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid
        return right