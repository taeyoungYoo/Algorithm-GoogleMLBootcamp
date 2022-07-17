class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)

        answer = []
        for i in range(len(nums)):                  # 배열 순차 탐색

            left, right = i + 1, len(nums) - 1      # 배열의 i를 제외한 나머지 배열의 첫 수와 끝 수 인덱스

            while left > 0 and right < len(nums) and left < right:      # 왼쪽, 오른쪽 인덱스를 한칸씩 옮기며 합 체크
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] == 0:
                    answer.append((nums[i], nums[left], nums[right]))
                    left += 1

        return set(answer)


nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))


# 풀이1. 중첩 for문 : Time Limit Exceeded
# class Solution:
#     def threeSum(self, nums):
#         nums = sorted(nums)
#
#         answer = []
#         for i, n1 in enumerate(nums):
#             for j, n2 in enumerate(nums[i + 1:]):
#                 n3 = -(n1 + n2)
#                 if n3 in nums[i + j + 2:]:
#                     answer.append((n1, n2, n3))
#
#         return set(answer)

# 풀이2. itertool 활용 : Time Limit Exceeded
# class Solution:
#     def threeSum(self, nums):
#         nums = sorted(nums)
#         result = set([items for items in itertools.combinations(nums, 3) if sum(items) == 0])
#
#         return result

