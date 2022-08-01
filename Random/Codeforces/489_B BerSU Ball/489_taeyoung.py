# 1 <= n, m <= 100
# time limit: 1 sec, memory: 256MB
# dancing skill should differ by at most 1
# runtime: 46ms
n = int(input())
boys = list(map(int, input().split()))
m = int(input())
girls = list(map(int, input().split()))

boys.sort()
girls.sort()

ret = 0
limit = 0
for boy in boys:
    for i in range(limit, len(girls)):
        if abs(boy - girls[i]) < 2:
            ret += 1
            limit = i + 1
            break
print(ret)