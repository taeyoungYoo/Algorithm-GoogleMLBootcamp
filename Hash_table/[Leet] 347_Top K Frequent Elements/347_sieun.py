from collections import Counter

# 시은 풀이 - 107ms
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [item for item, count in Counter(nums).most_common(k)]

# 교재 풀이 - 156ms
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*Counter(nums).most_common(k)))[0]