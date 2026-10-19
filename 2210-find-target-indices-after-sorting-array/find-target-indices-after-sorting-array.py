class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        """
        Time Complexity = O(n)
        Space Complexity = O(k) ; where k is target freq
        """
        n = len(nums)
        target_freq = 0
        less_freq = 0
        for num in nums:
            if num == target:
                target_freq += 1
            elif num < target:
                less_freq += 1
        if target_freq == 0:
            return []
        return [i for i in range(less_freq, less_freq + target_freq)]