#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 32_1143. Longest Common Subsequence.py
@time: 2025/4/25 上午10:31
@desc:
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j]表示text1[0:i-1] 与 text2[0:j-1] 的最长子序列长度
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]

        result = 0
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

                if dp[i][j] > result:
                    result = dp[i][j]
        return result


if __name__ == '__main__':
    s = Solution()