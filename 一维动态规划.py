from typing import List
import math


class Solution:
    # 70: 爬楼梯
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [1] * n
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

    # 198: 打家劫舍
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)
        for i in range(n):
            dp[i + 2] = max(dp[i + 1], dp[i] + nums[i])
        return dp[-1]

    # 139: 单词拆分
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            if not dp[i]:
                continue
            for word in wordDict:
                j = len(word)
                if i + j <= n and s[i : i + j] == word:
                    dp[i + j] = True
        return dp[-1]

    # 322:零钱兑换
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        for i in range(amount):
            for coin in coins:
                if i + coin <= amount:
                    dp[i + coin] = min(dp[i] + 1, dp[i + coin])
        return -1 if math.isinf(dp[-1]) else dp[-1]

    # 300: 最长递增子序列
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (n := len(nums))
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
