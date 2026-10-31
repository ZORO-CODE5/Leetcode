class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])

        if m == 1 and n == 1:
            return 1 if grid[0][0] == 0 else 0

        from_left = [[0] * n for _ in range(m)]
        from_top = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    if grid[0][0] == 0:
                        if n > 1:
                            from_left[0][1] = 1
                        if m > 1:
                            from_top[1][0] = 1
                    continue

                if i == m - 1 and j == n - 1:
                    return (from_left[i][j] + from_top[i][j]) % MOD

                if grid[i][j] == 0:
                    total_ways = (from_left[i][j] + from_top[i][j]) % MOD
                    if j + 1 < n:
                        from_left[i][j + 1] = total_ways
                    if i + 1 < m:
                        from_top[i + 1][j] = total_ways
                else:
                    if i + 1 < m:
                        from_top[i + 1][j] = from_left[i][j]
                    if j + 1 < n:
                        from_left[i][j + 1] = from_top[i][j]

        return 0