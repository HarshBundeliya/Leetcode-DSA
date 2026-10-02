class Solution: 
    def search(self, nums: list[int], target: int) -> int:
        s = 0
        e = len(nums)-1
        def binary_search(nums, s, e):
            if s > e:
                return -1
            mid = (s+e)//2
            if nums[mid] == target:
                return mid      
            elif nums[mid] > target:
                return binary_search(nums, s, mid-1)
            else:
                return binary_search(nums, mid+1, e)
        return binary_search(nums, s, e)