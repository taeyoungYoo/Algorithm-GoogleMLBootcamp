from collections import deque

def solution(priorities, location):
    # 인쇄 순서
    answer = 0
    # 인쇄 대기목록 (초기 순서, 우선 순위)
    waiting = deque([item for item in enumerate(priorities)])

    while waiting:
        # 가장 중요도가 높은 문서
        maxItem = max(waiting, key=lambda x: x[1])

        # 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
        item = waiting.popleft()

        # 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
        if item[1] < maxItem[1]:
            waiting.append(item)

        # 3. 그렇지 않으면 J를 인쇄합니다.
        else:
            answer += 1
            # 내가 요청한 문서인 경우 종료
            if item[0] == location:
                break

    return answer