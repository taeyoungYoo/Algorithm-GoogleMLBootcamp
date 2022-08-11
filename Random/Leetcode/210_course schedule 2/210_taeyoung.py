# Leetcode 210 Course schedule 2
# Topology sort with adj list -> O(V+E)
# runtime 142, memory: 15.4
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for link in prerequisites:
            adj_list[link[1]].append(link[0])
            in_degree[link[0]] += 1

        q = collections.deque()

        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        ret = []
        while q:
            now = q.popleft()
            ret.append(now)
            for next in adj_list[now]:
                in_degree[next] -= 1
                if in_degree[next] == 0:
                    q.append(next)
        if len(ret) != numCourses:
            return []
        else:
            return ret