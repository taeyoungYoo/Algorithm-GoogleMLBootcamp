class Solution:
    def trap(self, height):
        trapped = 0         # 저장된 물의 양

        top = max(height)           # 주어진 배열에서 가장 큰 값
        i_top = height.index(top)   # 주어진 배열에서 가장 큰 값의 위치

        left = height[:i_top]       # 가장 큰 값을 기준으로 왼쪽 배열
        right = height[i_top+1:]    # 가장 큰 값을 기준으로 오른쪽 배열

        while len(left) > 0:                                # 왼쪽 배열의 끝까지 탐색
            next_top_left = max(left)                       # 왼쪽 배열에서 가장 큰 값
            i_next_top_left = left.index(next_top_left)     # 왼쪽 배열에서 가장 큰 값의 위치

            width = len(left) - i_next_top_left - 1         # top과 next_top_left 사이의 너비
            block = sum(left[i_next_top_left+1:])           # 사이 너비 중 막힌 부분
            trapped += width * next_top_left - block        # top과 next_top_left 사이에 갖히는 물의 양 +

            left = left[:i_next_top_left]                   # 계산한 부분을 제외하고 더 왼쪽으로 탐색

        while len(right) > 0:                               # 오른쪽 배열 : 왼쪽 배열과 동일한 과정 수행
            next_top_right = max(right)
            i_next_top_right = right.index(next_top_right)

            width = i_next_top_right
            block = sum(right[:i_next_top_right])
            trapped += width * next_top_right - block

            right = right[i_next_top_right+1:]

        return trapped


height = [4,2,0,3,2,5]
print(Solution().trap(height))


### idea: bottom-up *Time Limit Exceeded

# height = np.array(height)
#
# trapped = 0
#
# while len(height) > 0:
#     while height[0] < 1:
#         height = np.delete(height, 0)
#         if len(height) == 0:
#             break
#     else:
#         while height[-1] < 1:
#             height = np.delete(height, -1)
#             if len(height) == 0:
#                 break
#
#     trapped += len([x for x in height if x <= 0])
#     height = height - 1
#
# print(trapped)