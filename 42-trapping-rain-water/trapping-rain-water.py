class Solution:
    def trap(self, height: list[int]) -> int:
        # Time Complexity = O(n)
        # Space Complexity = O(1)
        n = len(height)
        left_max = 0
        right_max = 0
        total_water = 0
        l = 0
        r = n - 1
        while l <= r:
            if height[l] < height[r]:
                left_max = max(left_max, height[l])
                total_water += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                total_water += right_max - height[r]
                r -= 1
        return total_water