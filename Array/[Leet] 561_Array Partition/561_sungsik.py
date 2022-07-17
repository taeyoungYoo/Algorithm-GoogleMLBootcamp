class Solution:
    def arrayPairSum(self, nums):
        nums = sorted(nums)     # 배열 정렬
        nums = nums[0::2]       # 홀수 번째 요소만 추출

        return sum(nums)        # 추출한 홀수 번째 요소의 합 반환


nums = [1,4,3,2]
print(Solution().arrayPairSum(nums))
