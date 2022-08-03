class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

    if len(prerequisites) == 0:       # 예외 처리: 선수 과목이 없는 경우 -> 과목 순서 그대로 반환
      return [i for i in range(numCourses)]

    in_degree = [0] * numCourses
    for node in prerequisites:        # 선수 과목이 필요한 경우 진입 차수 +1. O(n)
      in_degree[node[0]] += 1

    que = []
    for i in range(len(in_degree)):   # 선수 과목이 0인 과목을 큐에 추가. O(n)
      if in_degree[i] == 0:
        que.append(i)

    answer = []
    while que:    # O(n^2)
      now = que.pop(0)
      answer.append(now)

      out_degree = [x for x in prerequisites if x[1] == now]  # 진출 차수가 있는 경우
      for node in out_degree:                                 # 큐에 추가하고 진입 차수 -1
        in_degree[node[0]] -= 1
        if in_degree[node[0]] == 0:                           # 추가로 필요한 선수 과목이 없으면 큐에 추가
          que.append(node[0])

    if len(answer) != numCourses:     # 예외 처리: 순환이 있는 경우. -> 빈 리스트 반환환
      return []

    return answer

