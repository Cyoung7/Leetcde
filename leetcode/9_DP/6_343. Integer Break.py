#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 6_343. Integer Break.py
@time: 2025/4/23 上午11:39
@desc:
"""


class Solution:
    def integerBreak(self, n: int) -> int:

        # dp[i]表示数值i被拆分的最大乘积
        dp = [0] * (n+1)
        # dp[0] dp[1] 没有任何有意义
        dp[2] = 1

        for i in range(3, n+1):
            for j in range(1, i-1):
                # dp[i]不仅可以从dp[i-j] * j来，还可以(i-j) * j直接相乘
                dp[i] = max(dp[i], (i-j) * j, dp[i-j] * j)
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.integerBreak(10))
