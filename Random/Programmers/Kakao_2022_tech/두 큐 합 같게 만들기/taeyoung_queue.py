'''
    2021 Kakao Tech Internship 문제
    두 큐의 합 같게 만들기
    두 큐의 길이는 같으며 len(q) <= 300,000
'''

import collections

def solution(queue1, queue2):
    answer = 0
    # 데크 활용 O(1)
    q1 = collections.deque(queue1)
    q2 = collections.deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    if (sum1 + sum2) % 2 == 1:
        return -1
    target = (sum1 + sum2) // 2
    # 최대 반복 횟수 설정해서 무한 루프 방지
    # 루프마다 큐에 접근해서 sum을 구하면 비효율적(O(N)) -> 실제 pop, append 해주되 sum 변수 관리
    for i in range(3 * len(q1)):
        if sum1 == target or not q1 or not q2:
            break
        elif sum1 > sum2:
            val = q1.popleft()
            q2.append(val)
            sum1 -= val
            sum2 += val
        else:
            val = q2.popleft()
            q1.append(val)
            sum1 += val
            sum2 -= val
    answer = i
    if not q1 or not q2 or sum1 != target:
        answer = -1
    return answer