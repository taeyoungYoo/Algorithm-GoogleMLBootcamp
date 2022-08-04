'''
ㅇ문제
- 남,녀 댄스스킬이 적혀진 arr가 제공되고
- 남녀의 댄스스킬차이가 1 이하일 경우만 파트너가 된다. 
- 가능한 파트너 수?

ㅇ접근법 - 77ms
1. boys, girls 오름차순 정렬
2. 각각의 arr에 포인터 각각 하나씩 두고 (b : boy, g : girl)
3. 서로의 댄스스킬이 1이하로 차이나면 count 1씩 증가하고 포인터 오른쪽으로 이동(파트너 이뤘으니까 둘 다 이동)
4. boy나 girl중 작은쪽이 있으면 오른쪽으로 한칸씩 이동해서 높은수에 가까워 지도록 함
5. 한쪽의 index가 끝에 도달할때 까지
'''

# 46~77ms 시간복잡도 O(n^2) 으로 추정 - while 부분
#입력
n = int(input()) #boy 인원수 
boys = list(map(int,input().split())) # boy 댄스스킬 arr
m = int(input()) #gril 인원수
girls = list(map(int,input().split())) # gril 댄스스킬 arr

#sort - 포인터 개념 적용을 위해 오름차순 정렬, 정렬하지 않으면 문제가 제대로 풀리지 않음
boys.sort() # O(nlogn)
girls.sort() # O(nlogn)

#count using each pointer
b, g = 0, 0 #boy_pointer, girl_pointer 변수 선언
count = 0 # count 변수 선언 
# O(n^2) -> 최악의 경우 두 arr 끝까지 탐색할 가능성 있음
while b<n and g<m:   #한쪽의 index가 over될 경우 종료 
    #두 원소의 차가 1이하 (절대값 1이하)일 경우 count 증가 -> 포인터 둘다 이동
    if abs(boys[b]-girls[g]) <= 1:
        count += 1
        b += 1        
        g += 1
    # 소년들의 댄스스킬이 부족할 경우 다음 소년으로 이동 (포인터 우측이동)
    elif boys[b] < girls[g]:
        b += 1
    # 소녀들의 댄스스킬이 부족할 경우
    else :
        g += 1

#출력
print(count)
