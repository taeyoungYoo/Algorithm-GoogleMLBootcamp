'''
개발언어 - cpp,java,python 중 하나
직군 - backend, frontend 
경력 - junior, senior 
소울푸드 - chicken, pizza

'''

# 모든 경우에 대해서 tree형태로 생각할 수 있다.
# 언어 4가지 * 직군 3가지 * 경력 3가지 * 소울푸드 3가지 = 108가지 
# 모든 경우에 대해서 1차원 배열로 표현 가능함 
# 0000(----) -> 0,  3222(python/front/senior/pizza)>  81+18+6+2 -> 107 

# 모든 테이블(경우의 수)에 점수를 입력하고
# 쿼리에 해당하는 사람의 수를 bisect_left를 이용해 계산

#효율성 test -> 727ms~742ms
from bisect import bisect_left

def solution(info, query):
    # 매핑 정보 입력
    wmap = {'-':0, 'cpp':1, 'java':2, 'python':3,
                    'backend':1, 'frontend':2,
                    'junior':1, 'senior':2,
                    'chicken':1, 'pizza':2}
    
    slist = [[] for _ in range(4*3*3*3)]
        
    for string in info:
        # w -> ['java','backend','junior','pizza','150'] 
        w = string.split()
        
        arr = (wmap[w[0]]*3*3*3,    #언어
              wmap[w[1]]*3*3,       #직군
              wmap[w[2]]*3,         #경력
              wmap[w[3]])           #소울푸드
        score = int(w[4])           # 점수
        
        # info 모든 경우(항목마다 있고 없고)에 점수를 append
        for i in range(1<<4): # 쿼리 항목이 4개 1을 왼쪽으로 4번  00001 -> 10000(16)   i 값 : 0~15번 까지
            idx = 0
            for j in range(4):
                if i & (1 << j):  # j번째 원소가 있는 경우 
                    idx += arr[j]
            slist[idx].append(score)
    
    # 모든 경우의 수 오름차순 정렬 -> 뒤에 bisect_left 쓰려고
    for i in range(4*3*3*3):
        slist[i] = sorted(slist[i])
    
    answer = []
    for string in query:
        w = string.split() 
        # and로 분리하지 않는 이유 : 쿼리 맨마지막 소울푸드와 점수 사이에 and가 없음 
        # 인덱싱 번호를 0,2,4,6 으로 and를 무시하고 처리
        print(w)
        idx = wmap[w[0]]*3*3*3 + wmap[w[2]]*3*3 + wmap[w[4]]*3 + wmap[w[6]]
        score = int(w[7]) 
        answer.append(len(slist[idx]) - bisect_left(slist[idx], score)) 
        # bisect_left  ex) [100, 200, 300] 50을 추가시 0번째 인덱스에 넣어야 한다 
        # score(50) 보다 큰 사람이 원래 리스트 길이(3) - index(0) = 3 명 
        # score(250) 보다 큰 사람이 원래 리스트 길이(3) - index(2) = 1 명   
    return answer
