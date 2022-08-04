# time 46 ms, memory 0 kb
n = 4
boys = [1, 4, 6, 2]
m = 5
girls = [5, 1, 5, 7, 9]

boys.sort()
girls.sort()

answer = 0

for i in boys:
    if i-1 in girls:
        girls.remove(i-1)
        answer += 1
    elif i in girls:
        girls.remove(i)
        answer += 1
    elif i+1 in girls:
        girls.remove(i+1)
        answer += 1

print(answer)
