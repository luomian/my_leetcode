from typing import List


class Solution:
    # 120: 三角形最小路径和
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if (n := len(triangle)) == 1:
            return triangle[0][0]
        dp = [[triangle[0][0]] * (i + 1) for i in range(n)]
        for i, nums in enumerate(triangle[1:], start=1):
            for j in range(len(nums)):
                if j == 0:
                    dp[i][j] = dp[i - 1][0] + triangle[i][j]
                elif j == len(nums) - 1:
                    dp[i][j] = dp[i - 1][-1] + triangle[i][j]
                elif 0 < j < len(nums) - 1:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        return min(dp[-1])

    # 64 最小路径和
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[grid[0][0]] * n for _ in range(m)]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]

    # 63: 不同路径
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(0, m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    # 5 最长回文子串
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLen = 1
        maxLenS = s[0]
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        # [i:j+1]
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j] and ((j - i <= 2) or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j - i + 1 > maxLen:
                        maxLen = j - i + 1
                        maxLenS = s[i: j + 1]
        return maxLenS

    # 97: 交错字符串
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
