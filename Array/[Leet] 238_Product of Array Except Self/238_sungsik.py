class Solution:         # discuss 참고
    def productExceptSelf(self, nums):
        answer = []
        product = 1
        for i in range(len(nums)):
            answer.append(product)
            product = product * nums[i]

        product = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] = answer[i] * product
            product = product * nums[i]

        return answer



# 풀이 1. 중첩 for문 : Time Limit Exceeded
# answer = []
# for i in range(len(nums)):
#     tmp_nums = copy.deepcopy(nums)
#     tmp_nums.pop(i)
#     tmp_product = 1
#
#     if 0 in tmp_nums:
#         answer.append(0)
#     else:
#         for j in tmp_nums:
#             tmp_product *= j
#
#         answer.append(tmp_product)
#
# print(answer)


# 풀이 2. reduce : Time Limit Exceeded
# answer = []
# for i in range(len(nums)):
#     tmp_nums = copy.deepcopy(nums)
#     tmp_nums.pop(i)
#     answer.append(reduce(lambda x, y: x * y, tmp_nums))
#
# print(answer)
