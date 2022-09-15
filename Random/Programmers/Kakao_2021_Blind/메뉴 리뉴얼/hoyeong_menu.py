'''
단품으로만 제공하던 메뉴를 조합해서 
코스요리로 재구성 하여 제공

이전 각 손님들이 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성

규칙1 : 최소 2가지 이상의 단품메뉴
규칙2 : 최소 2명 이상의 손님으로부터 주문된 단품 메뉴
규칙3 : 가장 많이 주문된 조합
규칙4 : 메뉴 구성이 여러 개라면 모두 배열에 담는다.

orders -> 주문했던 단품메뉴
course -> 단품메뉴들의 갯수
result -> 오름차순 정렬 

'''

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    # course 순환
    for num in course:
        temp = [] 
        
        # orders 순환
        for order in orders:
            combi = combinations(sorted(order), num)   # num개 만큼의 조합결과 생성 
            temp += combi # 조합결과(combi, 튜플) temp 리스트에 extend
                
        counter = Counter(temp) # Counter 함수로 조합별 주문횟수 카운팅
        
        # 최소 2명 이상의 손님으로부터 주문된 경우에만
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(i) for i in counter if counter[i] == max(counter.values())] # 가장 많이 주문한 메뉴를 answer 추가
            
    return sorted(answer) # 오름차순 정렬
