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
                if s[i] == s[j] and ((j - i <= 2) or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i + 1 > maxLen:
                        maxLen = j - i + 1
                        maxLenS = s[i : j + 1]
        return maxLenS

    # 97: 交错字符串
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp[i][j]表示s1的前i个字符，s2的前j个字符能否构成s3的前i+j个字符
        lenOfS1, lenOfS2, lenOfS3 = len(s1), len(s2), len(s3)
        if lenOfS1 + lenOfS2 != lenOfS3:
            return False
        dp = [[False] * (lenOfS2 + 1) for _ in range(lenOfS1 + 1)]
        dp[0][0] = True
        for i in range(1, lenOfS1 + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = True
            else:
                break
        for j in range(1, lenOfS2 + 1):
            if s2[j - 1] == s3[j - 1]:
                dp[0][j] = True
            else:
                break
        for i in range(1, lenOfS1 + 1):
            for j in range(1, lenOfS2 + 1):
                if dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = True
                elif dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = True
        print(dp)
        return dp[-1][-1]

    # 72, 编辑距离
    def minDistance(self, word1: str, word2: str) -> int:
        pass

    # 21: 最大正方形
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    res = max(res, dp[i][j])
        return res * res

    # 72 编辑距离
    def minDistance72(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for j in range(1, len2 + 1):
            dp[0][j] = j
        for i in range(1, len1 + 1):
            dp[i][0] = i
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]
