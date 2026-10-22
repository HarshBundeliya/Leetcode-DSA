class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zero_idx = nums.index(0)

        forward = all((nums[i] + 1) % n == nums[(i + 1) % n] for i in range(n))
        reverse = all((nums[i] - 1) % n == nums[(i + 1) % n] for i in range(n))

        if forward:
            return min(zero_idx, n - zero_idx + 2) if zero_idx else 0

        if reverse:
            return min(zero_idx + 2, n - zero_idx)

        return -1