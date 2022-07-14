# 시은 풀이(교재 참고) - 338ms
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)

        # left[i]: nums[0]*nums[1]...*nums[i-1]
        left = [1 for _ in range(n)]
        # right[i]: nums[i+1]*nums[i+2]...*nums[-1]
        right = [1 for _ in range(n)]

        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]

        for i in reversed(range(0, n - 1)):
            right[i] = right[i+1] * nums[i+1]

        return [left[i] * right[i] for i in range(n)]

# 교재 풀이 - 334ms
class Solution2(object):
    def productExceptSelf(self, nums):
        out = []
        p = 1

        # out[i] = nums[0]*nums[1]...*nums[i-1]
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]

        p = 1

        # out[i] = nums[0]*nums[1]...*nums[i-1]*nums[i+1]*...nums[-1]
        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]

        return out
