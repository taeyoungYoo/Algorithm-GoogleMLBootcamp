# C++ friendly 코드
# Runtime: 61ms, memory: 14.3MB
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [0] * len(nums)
        ret = []
        def dfs(cnt: int, tmp: list):
            if cnt == len(nums):
                ret.append(tmp[:])
                return
            for i, val in enumerate(nums):
                if visited[i] == 1:
                    continue
                tmp.append(val)
                visited[i] = 1
                dfs(cnt+1, tmp)
                tmp.pop()
                visited[i] = 0
        dfs(0, [])
        return ret