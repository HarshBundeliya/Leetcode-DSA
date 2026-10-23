class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        """
        Time Complexity = O(n)
        Space Complexity = O(n)
        """
        n = len(nums)
        res = []
        for i in range(n):
            if i != nums[i]:
                res.append(nums[i])
        
        if not res:
            return 0
        
        k = res[0]
        for j in range(1,len(res)):
            k &= res[j]
        return k