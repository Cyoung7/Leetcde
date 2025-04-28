#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 28_714. Best Time to Buy and Sell Stock with Transaction Fee.py
@time: 2025/4/24 下午4:36
@desc:
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # dp[i][0]持有股票 手中的现金   dp[i][1]不持有股票 手中的现金
        dp = [[0, 0] for i in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0] - fee)  # 和122唯一区别：每一次卖掉需要-fee
        return dp[-1][1]
