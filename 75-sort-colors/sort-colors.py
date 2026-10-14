class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Time Complexity = O(n)
        Space Complexity = O(1)
        """
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        for i in range(d[0]):
            nums[i] = 0
        for i in range(d[0], d[0] + d[1]):
            nums[i] = 1
        for i in range(d[0] + d[1], d[0] + d[1] + d[2]):
            nums[i] = 2