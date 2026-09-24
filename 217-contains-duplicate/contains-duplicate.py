class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Time complexity = O(n)
        # Space complexity = O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False