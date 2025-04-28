#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 40_516. Longest Palindromic Subsequence.py
@time: 2025/4/25 下午3:13
@desc:
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        这道题使劲想一下，还是可以想到的
        :param s:
        :return:
        """
        # dp[i][j]：表示区间范围[i,j] （注意是左闭右闭）的最长回文子序列
        dp = [[0] * (len(s)) for _ in range(len(s))]

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = j-i+1
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1]
