# Stock Buy And Sell

# Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


class Solution():

    def getMaxProfitOne(self, arr):

        maxProfit, minPrice = 0, max(arr)
    
        for price in arr:
            if minPrice > price:
                minPrice = price
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice

        return maxProfit


    def getMaxProfitTwo(self, arr):

        maxProfit, minPrice = 0, max(arr)
    
        for price in arr:
            minPrice = min(minPrice, price)
            maxProfit = max(price-minPrice, maxProfit)

        return maxProfit


arr = [7, 1, 5, 3, 6, 4]
s1 = Solution()

maxProfit = s1.getMaxProfitOne(arr)
print(maxProfit)

maxProfit = s1.getMaxProfitTwo(arr)
print(maxProfit)