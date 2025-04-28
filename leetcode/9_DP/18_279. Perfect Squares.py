#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 18_279. Perfect Squares.py
@time: 2025/4/24 上午10:42
@desc:
"""
import sys


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0

        # 背包容量
        for i in range(1, n+1):
            # m是物品
            for j in range(1, n+1):
                m = j ** 2
                if m <= i:
                    dp[i] = min(dp[i], dp[i-m]+1)
                if m > i:
                    break
        return dp[n]
