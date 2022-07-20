import sys

def expand(s1_index: int, s2_index: int) -> int:
    count = 0
    while s1_index < len(str1) and s2_index < len(str2) and str1[s1_index] == str2[s2_index]:
        s1_index += 1
        s2_index += 1
        count += 1
    return count
    

str1 = input()
str2 = input()
result = 0
for i, s1 in enumerate(str1):
    for j, s2 in enumerate(str2):
        if s1 == s2:
            result = max(result, expand(i,j))

print(result)