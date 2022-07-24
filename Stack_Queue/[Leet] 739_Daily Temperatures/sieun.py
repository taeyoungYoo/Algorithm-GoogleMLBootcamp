class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = []  # (이전 날씨 인덱스, 이전 날씨 온도)

        for i, current in enumerate(temperatures):
            while stack and stack[-1][1] < current:
                j, prev = stack.pop()
                answer[j] = i - j
            stack.append((i, current))

        return answer
