class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        Time Complexity = O(n)
        Space Complexity = O(n)
        """
        n = len(heights)
        stack = []
        best = 0
        for i in range(n+1):
            h = heights[i] if i < n else 0

            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                area = height * (i - left -1)
                best = max(best, area)
            stack.append(i)
        return best