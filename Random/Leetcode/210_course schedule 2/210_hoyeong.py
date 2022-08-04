'''
문제
prerequisites[i] =  [a, b]   -> a를 듣기 위해서는 반드시 b를 들어야 한다. 
b가 선행 코드 (key 값이 된다)
모든 코스를 들을 수 있을 경우 코스를 나열
모든 코스를 듣지 못하는 경우 빈 list 리턴

input()
4
[[1,0],[2,0],[3,1],[3,2]]

graph = {0:[1,2], 1:[3], 2:[3]}

    -> 1 - 
0 -        ->3
    -> 2 -

  진입차수      q             ans
[0, 1, 1, 2] deque([0])      []
[0, 0, 0, 2] deque([1, 2])   [0]
[0, 0, 0, 1] deque([1])      [0, 2]
[0, 0, 0, 0] deque([3])      [0, 2, 1]
[0, 0, 0, 0] deque([])       [0, 2, 1, 3]

'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 위상정렬 - 133~189ms
        # 위상정렬 시간복잡도 : O(v+e) -> O(N)?
        graph = collections.defaultdict(list) # 그래프 초기화
        indegree = [0] * numCourses # 진입차수 초기화 
        ans, q = [], collections.deque() # 우선순위 큐?
        
        for a,b in prerequisites:
            graph[b].append(a) # b(선행과목)을 key값 으로 value list에 a를 append
            indegree[a] += 1 # a개수에 따라 진입차수
        # print(graph,indegree,ans,q)
        
        # 진입차수 0인값 q에 append
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
                        
        while q:            
            now = q.pop()    # 현재값 q에 pop
            ans.append(now)  # ans에 append
            for i in graph[now]:  # 1,2 순환하며 진입차수 줄여준다.
                indegree[i] -= 1
                if indegree[i] == 0: # 진입차수가 0이 되면 
                    q.append(i)      # q에 넣고 반복
        
        # 모든 강의를 들었으면, ans의 길이가 numCourses와 같기 때문에 ans를 리턴하고
        if len(ans) == numCourses:
            return ans
        # 아닌 경우 빈 list를 리턴한다.
        else:
            return []
