from collections import deque

def solution(priorities, location):
    '''
    중요도가 높은 문서를 언저 인쇄하는 프린터 개발
    1. 가장 앞에있는 문서(J) 꺼냄
    2. J 이후에 J보다 우선 순위가 하나라도 높은게 있으면 맨 뒤로 보냄
    3. 그렇지 않으면 J 출력
    '''
    ans = 0
    
    # 우선순위,순서 (n,i) tuple 형태를 원소로 가지는 deque 생성
    # ex)  [2,1,3,2] -> [(2,0), (1,1), (3,2), (2,3)]
    idx_prior = deque([(n,i) for i,n in enumerate(priorities)])  # O(n)
    

    # 시간 복잡도 O(n^2) 으로 추정 -  while반복문 * max()
    while idx_prior:  # O(n)
        # 최대값 갱신
        max_val = max(idx_prior)  # O(n)
        # 임시 비교값(J) 갱신
        tmp_val = idx_prior.popleft() # O(1)  *참고 pop(0) -> O(k) k:원소개수 , 상수는 무시
        
        # 비교값이 최대값이면? 
        if tmp_val[0] == max_val[0]: # O(1)
            ans += 1 # 출력순서 +1
            
            # 비교값의 순서가 지정한 location 값이면 반복문 즉시 종료 후 
            if tmp_val[1] == location:    # O(1) 
                break
        else:
            idx_prior.append(tmp_val)  # O(1)
    
    #ans 출력 순서 반환
    return 
