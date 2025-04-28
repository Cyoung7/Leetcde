#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 1_509. Fibonacci Number.py
@time: 2025/4/23 上午9:59
@desc:
"""


class Solution:
    def fib(self, n: int) -> int:
        """
        动态规划五部曲：
        确定dp数组（dp table）以及下标的含义
        确定递推公式
        dp数组如何初始化
        确定遍历顺序
        举例推导dp数组

        1.dp数组小标为0-n，dp(i)的i对应的斐波那契值
        2.地推公式 dp(i) = dp(i-2) + dp(i-1)
        3.初始化： dp(0) = 0 dp(1) = 1
        4.遍历顺序： 2-n
        5.举例 dp(2) = dp(0) + dp(1)
        :param n:
        :return:
        """
        if n <= 1:
            return n
        # dp table
        dp = [0 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
