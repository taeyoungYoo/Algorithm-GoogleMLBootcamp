'''
길이가 같은 두 개의 큐
하나의 큐를 골라(임의?) 원소 pop -> 다른큐에 insert 해서 두 큐의 합이 같을 때 까지

큐1, 큐2

큐1 = [3,2,7,2] -> 14
큐2 = [4,6,5,1] -> 16

두 큐의 합이 같아지려면 각각 15가 되어야 한다.
'''


from collections import deque

# 시간 초과 났었음 -> while 안에 예외처리(sum 함수를 넣으니까 시간 초과 발생)
def solution(queue1, queue2):
    answer = 0
    
    tmp = queue1 + queue2
    
    max_value = max(tmp)
    each_target = sum(tmp) // 2

    n = len(queue1)
    
    queue1, queue2 = deque(queue1), deque(queue2) #큐 생성
    sum1, sum2 = sum(queue1), sum(queue2)
    # 두 원소중 가장큰 원소의 값 > 모든 원소의 합/2 -> 불가능하다 -1 리턴
    # 예외처리1. - 모든 원소의 합이 홀수면 불가
    if sum(tmp)%2 == 1: 
        return -1

    # 예외처리2. - 가장 큰 값의 원소가 each_target 값보다 크면 불가
    if max_value > each_target:
        return -1
    
    while sum1 != sum2 and answer <= 4*n :
        answer += 1        
        
        # while 안에 함수를 쓰니까 시간이 기하급수적으로 늘어남
        # sum1 에다가 num을 더하고 빼주는 방식으로 사칙연산 적용시 시간 개선 가능
        if sum1 < sum2:
            num = queue2.popleft()
            sum1 += num
            sum2 -= num
            queue1.append(num)
        else:
            num = queue1.popleft()
            sum1 -= num
            sum2 += num
            queue2.append(num)

    return answer if answer <= 4*n else -1

# 다른 풀이 
# def solution(queue1, queue2):
#     # 예외처리 1
#     if sum(queue1+queue2) % 2 == 1:
#         return -1
    
#     # 슬라이딩 윈도우 인덱스
#     n = len(queue1)
#     l,r = 0, n
    
#     def get_num(idx):
#         idx %= 2 * n  # 인덱스 오버 나는거 방지 합친 큐의 길이로 나눠준다.
#         return queue1[idx] if idx < n else queue2[idx-n]
    
#     answer = 0 
#     sum1, sum2 = sum(queue1), sum(queue2)
#     while sum1 != sum2 and answer <= 3*n:
#         answer += 1
#         if sum1>sum2:
#             num = get_num(l)
#             sum1 -= num
#             sum2 += num
#             l += 1
#         else:
#             num = get_num(r)
#             sum1 += num
#             sum2 -= num
#             r += 1
#     return answer if answer <= 3*n else - 1
