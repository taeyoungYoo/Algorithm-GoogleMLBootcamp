# 시은 풀이 - 242ms
class Solution(object):
    def arrayPairSum(self, nums):
        # 오름차순으로 정렬하고 순차적으로 분할
        # [1, 2, 3, 4] => [(1, 2), (3, 4)]
        return sum([value for i, value in enumerate(sorted(nums)) if i % 2 == 0])

# 교재 풀이 - 323ms(?)
class Solution2(object):
    def arrayPairSum(self, nums):
        # 오름차순으로 정렬하고 순차적으로 분할
        # [1, 2, 3, 4] => [(1, 2), (3, 4)]
        return sum(sorted(nums)[::2])

