#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 36_115. Distinct Subsequences.py
@time: 2025/4/25 下午1:22
@desc:
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        非常难，特别的是状态转移方程
        :param s:
        :param t:
        :return:
        """
        dp = [[0] * (len(t) + 1) for _ in range(len(s)+1)]
        for i in range(1, len(s)):
            dp[i][0] = 1
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
