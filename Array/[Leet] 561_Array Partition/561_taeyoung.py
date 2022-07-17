# runtime: 411ms, memory: 16.8MB
# sort it first, then add the value in the even index
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ret = 0
        for i in range(0, len(nums), 2):
            ret += nums[i]
        return ret

# runtime: 422ms, memory: 16.8MB
# pythonic method
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])