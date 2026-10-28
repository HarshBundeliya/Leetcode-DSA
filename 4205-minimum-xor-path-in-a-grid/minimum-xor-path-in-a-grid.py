# class Solution:
#     def minCost(self, grid: list[list[int]]) -> int:
#         """
#         Time Complexity = O(P(m+n)), , where P = C(m + n - 2, m - 1) is the number of valid paths.
#         Auxiliary space: O(m+n) for the recursion stack.
#         """
#         m, n = len(grid), len(grid[0])
#         min_xor = float("inf")

#         def dfs(row, col, path_xor):
#             nonlocal min_xor

#             path_xor ^= grid[row][col]

#             # Reached the bottom-right cell
#             if row == m - 1 and col == n - 1:
#                 min_xor = min(min_xor, path_xor)
#                 return

#             # Move down
#             if row + 1 < m:
#                 dfs(row + 1, col, path_xor)

#             # Move right
#             if col + 1 < n:
#                 dfs(row, col + 1, path_xor)

#         dfs(0, 0, 0)
#         return min_xor


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        """
        Time Complexity: O(m * n * 1024)
        Space Complexity: O(n * 1024)
        """
        m, n = len(grid), len(grid[0])

        # dp[j] stores XOR values achievable at the current cell.
        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                value = grid[i][j]

                if i == 0 and j == 0:
                    dp[j] = {value}
                    continue

                current = set()

                # Paths arriving from above.
                if i > 0:
                    for x in dp[j]:
                        current.add(x ^ value)

                # Paths arriving from the left.
                if j > 0:
                    for x in dp[j - 1]:
                        current.add(x ^ value)

                dp[j] = current

        return min(dp[n - 1])
