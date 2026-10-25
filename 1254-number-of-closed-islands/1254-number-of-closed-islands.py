class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:

        def markconnectedlands(grid,r,c):
            if(r<0 or r>=len(grid) or c<0 or c>=len(grid[r])):
                return
            if grid[r][c]==-1 or grid[r][c]==1:
                return
            
            grid[r][c]=-1
            markconnectedlands(grid,r-1,c)
            markconnectedlands(grid,r+1,c)
            markconnectedlands(grid,r,c-1)
            markconnectedlands(grid,r,c+1)
        rows=len(grid)
        cols=len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c]==0) and r==0 or c==0 or r==rows-1 or c==cols-1:
                    markconnectedlands(grid,r,c)
        
        islands=0
        for r in range (1,rows-1):
            for c in range(1,cols-1):
                if grid[r][c]==0:
                    islands+=1
                markconnectedlands(grid,r,c)
        return islands
       