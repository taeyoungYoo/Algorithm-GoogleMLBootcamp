from collections import deque


def solution(queue1, queue2):
  answer = 0

  queue1 = deque(queue1)
  queue2 = deque(queue2)

  sum_q1 = sum(queue1)
  sum_q2 = sum(queue2)

  max_cnt = len(queue1) * 3

  while (queue1 and queue2) and max_cnt != answer:
    if sum_q1 == sum_q2:
      return answer
    elif sum_q1 > sum_q2:
      tmp = queue1.popleft()
      queue2.append(tmp)
      sum_q1 -= tmp
      sum_q2 += tmp
    elif sum_q1 < sum_q2:
      tmp = queue2.popleft()
      queue1.append(tmp)
      sum_q1 += tmp
      sum_q2 -= tmp
    answer += 1

  return -1

queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]
# expect : 7

print(solution(queue1, queue2))
