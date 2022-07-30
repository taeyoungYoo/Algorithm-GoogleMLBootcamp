class Solution:
    grid: List[List[str]]

    def dfs(self, i: int, j: int):
        if i < 0 or i >= len(self.grid) or j < 0 or j >= len(self.grid[0]) or self.grid[i][j] == '0':
            return
        self.grid[i][j] = '0'
        self.dfs(i + 1, j)
        self.dfs(i - 1, j)
        self.dfs(i, j + 1)
        self.dfs(i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(i, j)
                    ret += 1
        return ret