from collections import deque


def solution(priorities, location):
    priorities = deque(priorities)

    for i in range(len(priorities)):
        priorities[i] = (i, priorities[i])      # priorities 데크의 요소를 (index, value)인 pair 값으로 변경

    answer = 0
    while True:
        J = priorities.popleft()                # 현재 문서
        flag = True

        for i in range(len(priorities)):
            if J[1] < priorities[i][1]:         # 현재 문서보다 우선순위가 높은 경우
                priorities.append(J)            # 현재 문서를 대기열 맨 뒤로 이동
                flag = False
                break

        if flag == True:                        # 현재 문서가 우선순위가 가장 높은 경우
            answer += 1                         # 출력 순서(answer) +1
            if J[0] == location:                # 만약 현재 문서의 index가 location과 같으면 반복문 종료
                break

    return answer


priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))
# expect: 5


# 풀이 1. 런타임 에러. 정확성 85 (17/20)
# def solution(priorities, location):
#
#     pri_loc = deque()
#     for i in range(len(priorities)):
#         pri_loc.append((i, priorities[i]))        # (index, value)인 pair 값을 pri_loc에 추가
#
#     answer = 0
#     while pri_loc:
#         J = pri_loc.popleft()                     # pri_loc 에서 가장 앞의 문서 pop
#
#         if J[1] < max([x[1] for x in pri_loc]):   # 현재 문서보다 우선순위가 높은 문서가 큐에 있을 경우 맨 뒤로 이동
#             pri_loc.append(J)
#         else:                                     # 현재 문서의 우선순위가 가장 높은 경우
#             answer += 1                           # 출력 순서(answer) +1
#
#             if J[0] == location:                  # 만약 현재 문서의 index가 location과 같으면 반복문 종료
#                 break
#
#     return answer


# 풀이 3. 통과
# def solution(priorities, location):
#
#     pri_loc = deque()
#     for i in range(len(priorities)):
#         pri_loc.append((i, priorities[i]))        # (index, value)인 pair 값을 pri_loc에 추가
#
#     answer = 0
#     while pri_loc:
#         J = pri_loc.popleft()                     # pri_loc 에서 가장 앞의 문서 pop
#
#         if any(J[1] < x[1] for x in pri_loc):     # 현재 문서보다 우선순위가 높은 문서가 큐에 있을 경우 맨 뒤로 이동
#             pri_loc.append(J)
#         else:                                     # 현재 문서의 우선순위가 가장 높은 경우
#             answer += 1                           # 출력 순서(answer) +1
#
#             if J[0] == location:                  # 만약 현재 문서의 index가 location과 같으면 반복문 종료
#                 break
#
#     return answer
