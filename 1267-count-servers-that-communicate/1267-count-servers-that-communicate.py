class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rows = [0] * m
        cols = [0] * n

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1

        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if rows[r] > 1 or cols[c] > 1:
                        ans += 1

        return ans