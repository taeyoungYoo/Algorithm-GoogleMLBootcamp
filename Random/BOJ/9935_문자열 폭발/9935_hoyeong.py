# 시간 660ms 
def explosion_string1(s1:str, s2:str) -> str:
    '''
    - 첫번째 문자열에 폭발 문자열(2번째 입력) 포함하는 경우,
      첫번째 문자열에 포함된 폭발 문자열 제거,
      남아있는 문자열 반환
    - 첫번째 문자열이 비어있을경우 'FRULA' 반환
    '''
    ans = []
    len_s2 = len(s2) # 폭발 문자열 길이 (나중에 슬라이싱에 사용)
    
    # 첫번째 문자열 순환 - 시간복잡도 O(n^3) 인가?
    for c in s1:  # O(n) 
        ans.append(c) # O(1)
        if ''.join(ans[-len_s2:]) == s2: # O(n) join * O(len(s2)) 슬라이싱
            del ans[-len_s2:]  # O(n) del * O(len(s2)) 슬라이싱

    if ans:
        return ''.join(ans)
    else:
        return 'FRULA'        

print(explosion_string1(s1=input(), s2=input()))
