# runtime: 35ms, memory: 14MB
# counter를 사용해 해결

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = collections.Counter(stones)
        ret = 0
        for jewel in jewels:
            ret += counter[jewel]
        return ret

# 책 풀이
# runtime: 55MB, memory 13.8
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        for char in stones:
            freqs[char] += 1

        for char in jewels:
            count += freqs[char]

        return count