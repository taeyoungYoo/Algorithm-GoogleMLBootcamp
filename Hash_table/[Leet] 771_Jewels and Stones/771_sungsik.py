# runtime 58 ms (24.65 %), memory 13.8 mb (96.59 %)
class Solution:
  def numJewelsInStones(self, jewels: str, stones: str) -> int:
    return sum(s in jewels for s in stones)


# 풀이 1. 그냥 for + string 처리
# runtime 42 ms (69.50 %), memory 13.8 mb (58.50 %)
# class Solution:
#   def numJewelsInStones(self, jewels: str, stones: str) -> int:
#     answer = 0
#     for j in stones:
#       if j in jewels:
#         answer += 1
#     return answer

# 풀이 2. 해시맵
# runtime 64 ms (12.83 %), memory 13.9 mb (58.50 %)
# class Solution:
#   def numJewelsInStones(self, jewels: str, stones: str) -> int:
#     hashMap = {}
#     for i in jewels:
#       hashMap[i] = 0
#
#     for i in stones:
#       if i in hashMap.keys():
#         hashMap[i] += 1
#
#     return sum(hashMap.values())
