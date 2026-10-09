class Solution:
    def trap(self, height: list[int]) -> int:
        # Time Complexity = O(n)
        # Space Complexity = O(n)
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        current_left_max = 0
        current_right_max = 0
        l = 0
        r = n - 1
        while l < n and r > -1:
            current_left_max = max(current_left_max, height[l])
            left_max[l] = current_left_max
            l += 1
            current_right_max = max(current_right_max, height[r])
            right_max[r] = current_right_max
            r -= 1
        
        total_water = 0
        for i in range(len(height)):
            water = max(0, min(left_max[i], right_max[i]) - height[i])
            total_water += water
        
        return total_water