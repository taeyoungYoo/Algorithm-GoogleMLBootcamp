# Wrong answer on test 20...

from collections import defaultdict

# the number of boys
n = int(input())

# boy's dancing skills
boys = list(map(int, input().split()))

# the number of girls
m = int(input())

# girl's dancing skills
girls = list(map(int, input().split()))

# 소년: [소녀] 
pairs = defaultdict(list)

for boy_num, boy_skill in enumerate(boys):
    for girl_num, girl_skill in enumerate(girls):
        if abs(boy_skill - girl_skill) <= 1:
            pairs[boy_num].append(girl_num)

# 짝지어진 소녀의 번호
visited = []

for boy in sorted(list(pairs), key=lambda x: len(pairs[x])):
    for girl in pairs[boy]:
        if girl not in visited:
            visited.append(girl)
            break


print(len(visited))