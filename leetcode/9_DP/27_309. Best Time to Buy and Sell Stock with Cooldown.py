#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 27_309. Best Time to Buy and Sell Stock with Cooldown.py
@time: 2025/4/24 下午3:28
@desc:
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        太难了
        没刷过，保准做不出来
        :param prices:
        :return:
        """
        if not prices:
            return 0

        n = len(prices)
        # dp[i][0]: 手上持有股票的最大收益
        # dp[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
        # dp[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = -prices[0]
        
        for i in range(1, n):
            # 前一天持有，（或者前一天不持有，且今天不在冷冻期）
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])

        return max(dp[n - 1][1], dp[n - 1][2])
