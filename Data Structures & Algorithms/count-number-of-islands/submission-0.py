class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def exploreIsland(i, j):
            if grid[i][j] == "0":
                return
            print(i,j)
            visited[i][j] = True
            if i > 0 and not visited[i-1][j]:
                exploreIsland(i-1, j)
            if i < len(grid)-1 and not visited[i+1][j]:
                exploreIsland(i+1, j)
            if j > 0 and not visited[i][j-1]:
                exploreIsland(i, j-1)
            if j < len(grid[0])-1 and not visited[i][j+1]:
                exploreIsland(i, j+1)

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    exploreIsland(i, j)
                    islands += 1
        
        return islands