class Solution: 
    def search(self, nums: list[int], target: int) -> int:
        # Time Complexity = O(log(n))
        # Space Complexity = O(1)
        s = 0
        e = len(nums)-1
        while s <= e:
            mid = (s+e)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1 
        return -1