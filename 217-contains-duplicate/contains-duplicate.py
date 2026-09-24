class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Time complexity = O(n)
        # Space complexity = O(n)
        count_map = {}
        for num in nums:
            if num in count_map:
                return True
            else:
                count_map[num] = 1
        return False