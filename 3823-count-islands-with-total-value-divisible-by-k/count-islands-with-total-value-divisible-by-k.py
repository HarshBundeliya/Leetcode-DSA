
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        """
        Time Complexity = O(m*n)
        Space Complexity = O(m*n)
        """
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        island_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 or visited[r][c]:
                    continue

                stack = [(r, c)]
                visited[r][c] = True
                island_sum = 0

                while stack:
                    x, y = stack.pop()
                    island_sum += grid[x][y]

                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy

                        if (0 <= nx < rows and
                            0 <= ny < cols and
                            grid[nx][ny] > 0 and
                            not visited[nx][ny]):
                            stack.append((nx, ny))
                            visited[nx][ny] = True

                if island_sum % k == 0:
                    island_count += 1

        return island_count