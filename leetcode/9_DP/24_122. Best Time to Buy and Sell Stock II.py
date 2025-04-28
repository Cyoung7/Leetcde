#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 24_122. Best Time to Buy and Sell Stock II.py.py
@time: 2025/4/24 下午3:29
@desc:
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        贪心实现, 贪心思想
        :param prices:
        :return:
        """
        result = 0
        for i in range(1, len(prices)):
            # 核心思想就是第一天买第二天卖，吃到所有的波段利润，就是最大盈利
            if prices[i] - prices[i-1] > 0:
                result += (prices[i] - prices[i-1])
        return result


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        """
        DP实现
        :param prices:
        :return:
        """
        # dp[i] 第i天的最大利润
        dp = [0] * (len(prices))

        for i in range(1, len(prices)):
            dp[i] = max(dp[i-1], dp[i-1]+(prices[i] - prices[i-1]))
        return dp[-1]


class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        """
        DP实现, dp思想,
        看起来和Solution代码差不多，思想不一样
        :param prices:
        :return:
        """
        # dp 第i天的最大利润
        # 这里直接把数组简化了
        dp = 0

        for i in range(1, len(prices)):
            dp = max(dp, dp + (prices[i] - prices[i-1]))
        return dp


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp
        :param prices:
        :return:
        """
        # dp[i][0]持有股票 手中的现金   dp[i][1]不持有股票 手中的现金
        dp = [[0, 0] for i in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])
        return dp[-1][1]
