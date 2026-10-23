class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        """
        Time Complexity = O(n)
        Space Complexity = O(1)
        """
        n = len(nums)
        k = -1
        for i in range(n):
            if i != nums[i]:
                if k == -1:
                    k = nums[i]
                else:
                    k &= nums[i]
        
        if k == -1:
            return 0
    
        return k