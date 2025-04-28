#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 25_123. Best Time to Buy and Sell Stock III.py
@time: 2025/4/24 下午2:47
@desc:
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        非常难
        dp[i][0]: 第i天进行第一次买进，所剩的金额
        dp[i][1]: 第i天进行第一次卖出，所剩的金额
        dp[i][2]: 第i天进行第二次买进，所剩的金额
        dp[i][3]: 第i天进行第二次卖出，所剩的金额
        :param prices:
        :return:
        """
        len_price = len(prices)

        dp = [[0] * 4 for _ in range(len_price)]

        dp[0][0] = -prices[0]
        dp[0][2] = -prices[0]
        for i in range(1, len_price):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1]-prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2]+prices[i])
        return dp[-1][-1]