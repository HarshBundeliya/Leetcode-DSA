class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        """
        Time Complexity: O(m * n)
        Space Complexity: O(n)
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # down[j]: paths entering the current cell from above.
        # right: paths entering the current cell from the left.
        down = [0] * n

        for i in range(m):
            right = 1 if i == 0 else 0

            for j in range(n):
                from_left = right
                from_top = down[j]

                # Destination reached.
                if i == m - 1 and j == n - 1:
                    return (from_left + from_top) % MOD

                if grid[i][j] == 1:
                    # Mirror: left-entering paths go down,
                    # top-entering paths go right.
                    right = from_top
                    down[j] = from_left
                else:
                    # Empty cell: paths can move either right or down.
                    total = (from_left + from_top) % MOD
                    right = total
                    down[j] = total

        return 0