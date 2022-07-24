class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         #1. 부르트 포스 - 시간 초과
#         max_price = 0
#         for i, price in enumerate(prices):
#             for j in range(i, len(prices)):
#                 max_price = max(prices[j]-price, max_price)
                
#         return max_price
    
        #2. 저점과 현재 값과의 차이 계산
        # maxsize 라는거 처음 봄
        profit = 0
        min_price = sys.maxsize
        
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        
        return profit
