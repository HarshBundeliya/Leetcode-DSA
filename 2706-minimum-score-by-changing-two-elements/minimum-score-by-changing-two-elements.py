class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        """
        Time Complexity = O(nlogn)
        Space Complexity = O(n)

        We don't need to calculate the low score separately 
        because we can always make it zero by changing two elements to the same value.
        """
        if len(nums) <4:
            return 0
        
        nums.sort()

        C1 = nums[-1] - nums[2]
        C2 = nums[-3] - nums[0]
        C3 = nums[-2] - nums [1]
        return min(C1,C2,C3)