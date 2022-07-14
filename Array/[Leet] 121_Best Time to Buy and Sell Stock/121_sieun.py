# 시은 풀이 - 시간 초과
class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0

        for i, buy_price in enumerate(prices[:-1]):
            sell_price = max(prices[i + 1:])
            profit = sell_price - buy_price
            max_profit = max(profit, max_profit)

        return max_profit

# 시은 풀이 - 1068ms
class Solution2(object):
    def maxProfit(self, prices):
        n = len(prices)

        # buy[i]: min(buy[i-1], prices[i])
        #      : i번째 날까지의 최저점
        buy = [prices[0]] + [0 for i in range(n - 1)]

        for i in range(1, n):
            buy[i] = min(buy[i - 1], prices[i])

        # sell[i]: max(sell[i+1], prices[i])
        #        : i번째 날부터의 최고점
        sell = [0 for i in range(n - 1)] + [prices[-1]]

        for i in reversed(range(0, n - 1)):
            sell[i] = max(sell[i + 1], prices[i])

        # profit[i]: sell[i] - buy[i]
        #          : i번째 날 최고 수익
        profit = [sell[i] - buy[i] for i in range(n)]

        # 최고 수익 반환
        return max(profit)

# 교재 풀이 - 1715ms
class Solution2(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_price = sys.maxsize

        for price in prices:
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)

        return max_profit

