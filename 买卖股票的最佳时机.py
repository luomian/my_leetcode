from functools import cache
from typing import List
from math import inf


class Solution:
    # 121 买卖股票的最佳时机1
    def maxProfit1(self, prices: List[int]) -> int:
        profit, cur_buy_price = 0, inf
        for price in prices:
            if price > cur_buy_price:
                profit = max(profit, price - cur_buy_price)
            else:
                cur_buy_price = price
        return profit

    # 122 买卖股票的最佳时机2
    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i: int, hold: bool):
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
            else:
                return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])

        return dfs(n - 1, False)

    # 309 买卖股票最佳时机含冷冻期
    def maxProfitFrozen(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i: int, hold: bool):
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, True), dfs(i - 2, False) - prices[i])
            else:
                return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])

        return dfs(n - 1, False)

    # 188 买卖股票的最佳时机4
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i: int, j: int, hold: bool):
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, k, True), dfs(i - 1, j, False) - prices[i])
            else:
                return max(dfs(i - 1, k, False), dfs(i - 1, j - 1, True) + prices[i])

        return dfs(n - 1, k, False)
