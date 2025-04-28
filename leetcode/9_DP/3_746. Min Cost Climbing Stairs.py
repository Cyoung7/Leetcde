#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 3_746. Min Cost Climbing Stairs.py
@time: 2025/4/23 上午10:28
@desc:
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
                1.dp数组小标为0-(n-1)，dp(i)对应i层楼梯爬之后支付的最小费用
                2.地推公式 dp(i) = min(dp(i-2), dp(i-1)) + cost[i]
                3.初始化： dp(0) = cost[0] dp(1) = cost[1]
                4.遍历顺序： 2-(n-1)
                5.举例 dp(3) = dp(1) + dp(2)
        :param cost:
        :return:
        """
        len_n = len(cost)

        dp = [0 for _ in range(len_n)]
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len_n):
            dp[i] = min(dp[i-2], dp[i-1]) + cost[i]
        return min(dp[-1], dp[-2])


class Solution1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
                1.dp数组小标为0-(n)，dp(i)爬到第i层需要的最小费用
                2.地推公式 dp(i) = min(dp(i-2)+cost[i-2], dp(i-1)+cost[i-1])
                3.初始化： dp(0) = cost[0] dp(1) = cost[1]
                4.遍历顺序： 2-(n-1)
                5.举例 dp(3) = dp(1) + dp(2)
        :param cost:
        :return:
        """
        len_n = len(cost)

        dp = [0 for _ in range(len_n+1)]
        dp[0] = 0
        dp[1] = 0

        for i in range(2, len_n+1):
            dp[i] = min(dp[i - 2] + cost[i-2], dp[i - 1] + cost[i-1])
        return dp[-1]
