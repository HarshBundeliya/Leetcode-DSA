class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        Time Complexity = O(n)
        Space Complexity = O(n)

        The stack stores indices of smaller bars. 
        After popping, the new stack top tells us where the rectangle must stop on the left.
        """
        n = len(heights)
        best = 0
        stack = []
        for i in range(n+1):
            curr = heights[i] if i < n else 0
            while stack and heights[stack[-1]] >= curr:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                area = height * width
                best = max(best, area)
            stack.append(i)
        return best