from collections import defaultdict

# 교재 풀이
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        for a, b in sorted(tickets):
            graph[a].append(b)
            
        route = []
        
        def dfs(a):
            # 첫 번째 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)
            
        dfs('JFK')
        
        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]