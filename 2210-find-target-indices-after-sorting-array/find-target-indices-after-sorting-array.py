class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        """
        Time Complexity = O(nlog(n))
        Space Complexity = O(1)
        """
        n = len(nums)
        nums.sort()
        l = 0
        r = n-1
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                temp = mid
                while temp>=0 and target == nums[temp]:
                    temp-=1
                temp_2 = temp + 1
                result = []
                while temp_2<n and target == nums[temp_2]:
                    result.append(temp_2)
                    temp_2+=1
                return result
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return []