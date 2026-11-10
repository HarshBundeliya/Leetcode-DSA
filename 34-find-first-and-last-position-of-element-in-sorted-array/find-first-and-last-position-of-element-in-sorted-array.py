class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """
        Time Complexity = O(logn)
        Space Complexity = o(1)

        Remember this binary search rule:
        - When updating right = mid, use the lower midpoint.
        - When updating left = mid, use the upper midpoint.
        """
        n = len(nums)
        output = [-1,-1]
        
        left = 0
        right = n-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if 0<=right<=n-1 and nums[right] == target:
             output[0] = right

        left = 0
        right = n-1
        while left < right:
            mid = (left+right+1)//2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        if 0<=left<=n-1 and nums[left] == target:
             output[1] = left

        return output