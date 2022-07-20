# runtime: 341ms, memory: 21.2MB
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        acc_mul = []
        for i in nums:
            acc_mul.append(p)
            p *= i
        p = 1
        for i in range(len(nums)-1, -1, -1):
            acc_mul[i] *= p
            p *= nums[i]
        return acc_mul