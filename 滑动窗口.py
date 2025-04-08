from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass

    # 209：长度最小的子数组
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        ans = n + 1
        currentSum = 0
        for right in range(n):
            currentSum += nums[right]
            while currentSum >= target:
                ans = min(ans, right - left + 1)
                currentSum -= nums[left]
                left += 1
        return ans if ans <= n else 0
