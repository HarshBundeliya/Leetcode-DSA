class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Time Complexity = O(logn)
        Space Complexity = O(1)

        When the target is not in the sorted half, 
        discard that entire half and search the other half.
        """
        n = len(nums)
        start = 0
        end = n-1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid

            # Left half is sorted
            elif nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid-1
                else:
                    start = mid+1

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1