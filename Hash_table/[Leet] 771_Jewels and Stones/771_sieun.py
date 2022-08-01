# 시은 풀이 - 66ms
from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # stones counter
        stones = Counter(stones)

        # calculate
        answer = 0
        
        for jewel in jewels:
            answer += stones[jewel]
        
        return answer

# 교재 풀이 - 58ms
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in Jewels for stone in stones)