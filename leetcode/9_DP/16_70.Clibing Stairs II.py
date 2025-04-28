#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 16_70.Clibing Stairs II.py
@time: 2025/4/24 上午9:58
@desc: https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0070.%E7%88%AC%E6%A5%BC%E6%A2%AF%E5%AE%8C%E5%85%A8%E8%83%8C%E5%8C%85%E7%89%88%E6%9C%AC.md
"""


class Solution:
    def climbStairs(self, n: int, m: int) -> int:
        """
        这是一道完全背包，求排列的题
        :param n:
        :param m:
        :return:
        """
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            # 这里的j就是物品，而非简单的idx
            for j in range(1, m + 1):
                if i >= j:
                    dp[i] += dp[i - j]
        return dp[n]
