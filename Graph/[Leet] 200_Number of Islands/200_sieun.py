class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 알고리즘 수행 함수 (grid[i][j]가 속하는 섬을 모두 '#'으로 마킹하는 함수)
        def get_answer(i=0, j=0):
            # 범위를 벗어난 경우 
            if i < 0 or j < 0 or i == n or j == m or grid[i][j] != '1':
                return 
            
            # 마킹 
            grid[i][j] = '#'
                    
            # 상하좌우 탐색
            get_answer(i+1, j)
            get_answer(i-1, j)
            get_answer(i, j+1)
            get_answer(i, j-1)
       
        # 섬의 개수 
        answer = 0
        
        # 행과 열의 개수
        n, m = len(grid), len(grid[0])
        
        for i in range(n):
            for j in range(m):
                # 섬이 발견된 경우 
                if grid[i][j] == '1':
                    # 해당 섬 마킹 
                    get_answer(i, j)
                    # 개수 추가 
                    answer += 1
        
        return answer