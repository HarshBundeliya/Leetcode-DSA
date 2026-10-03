class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Time Complexity = O(nlogn) + O(n^2) = O(n^2)
        # Space Complexity = O(1)
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                if current_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                elif current_sum < 0:
                    l+=1
                else:
                    r-=1
        return res