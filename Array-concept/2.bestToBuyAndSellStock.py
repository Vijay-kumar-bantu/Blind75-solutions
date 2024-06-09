"""
Easy category
leetcode link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

def maxProfit(prices: list[int]) -> int:
        #intializing maximum profit and minimum buy index to 0
        max_profit = min_buy = 0
        
        for i in range(1,len(prices)):
            #checking current price
            current_profit = prices[i]-prices[min_buy]
            
            #updating the maximum profit if it current profit is great
            if current_profit>max_profit:
                max_profit=current_profit
            
            #updating the minmum buy to the current index if current index is less
            if prices[i]<prices[min_buy]:
                min_buy = i

        return max_profit


#Example
prices = [7,1,5,3,6,4]

#output should be 5 for above example
print(maxProfit(prices))