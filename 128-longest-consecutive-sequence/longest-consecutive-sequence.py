class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        Time complexity = O(n)
        Space Complexity = O(n)
        """
        bag = set(nums)
        best = 0
        for num in bag:
            if num - 1 in bag:
                continue
            current_best = 1
            while num + current_best in bag:
                current_best += 1
            best = max(best, current_best)
        return best