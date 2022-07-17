class Solution:
    def maxProfit(self, prices):
        buy = 0         # 매수한 날짜 인덱스
        profit = 0      # 이익

        for i in range(1, len(prices)):             # 주어진 전체 거래일에 대한 탐색 : o(n)
            if prices[i] - prices[buy] > profit:    # 과거 매수한 가격보다 현재 가격이 더 비싸고 현재 profit보다 크면
                profit = prices[i] - prices[buy]    # 최대 이익 갱신
            elif prices[i] < prices[buy]:           # 과거 매수한 가격보다 현재 가격이 더 싸면 매수한 날짜 인덱스 갱신
                buy = i

        return profit


prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))


# 풀이 1 : Time Limit Exceeded
# class Solution:
#     def maxProfit(self, prices):
#
#         profit = 0
#         while len(prices) > 1:
#             buy = prices[0]
#             if max(prices[1:]) - buy > 0:
#                 profit = max(profit, max(prices[1:]) - buy)
#             prices = prices[1:]
#
#         return profit
