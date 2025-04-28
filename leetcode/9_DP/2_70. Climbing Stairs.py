#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 2_70. Climbing Stairs.py
@time: 2025/4/23 上午10:17
@desc:
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
                1.dp数组小标为1-n，dp(i)对应i层楼梯的爬法
                2.地推公式 dp(i) = dp(i-2) + dp(i-1)
                3.初始化： dp(1) = 1 dp(2) = 2
                4.遍历顺序： 2-n
                5.举例 dp(3) = dp(1) + dp(2)
        :param n:
        :return:
        """
        if n <= 2:
            return n
        # dp table
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
