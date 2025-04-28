#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 26_188. Best Time to Buy and Sell Stock IV.py
@time: 2025/4/24 下午2:57
@desc:
"""
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        一维dp数组处理，非常抽象
        :param k:
        :param prices:
        :return:
        """
        len_price = len(prices)

        # j = 0-k
        # 2*j:buy 2*j+1:sell
        dp = [0] * 2 * k
        for i in range(k):
            dp[2*i] = -prices[0]

        for i in range(1, len_price):
            for j in range(k):
                # buy
                if j == 0:
                    dp[0] = max(dp[0], -prices[i])
                else:
                    dp[2*j] = max(dp[2*j], dp[2*j-1]-prices[i])

                # sell
                dp[2*j+1] = max(dp[2*j+1], dp[2*j]+prices[i])

        return dp[-1]


class Solution1:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        这里用二维的dp数组来处理，更好理解
        这里用两次来举例，方便写状态转移函数
        #             dp[i][0] = max(dp[i-1][0], -prices[i])
        #             dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        #             dp[i][2] = max(dp[i-1][2], dp[i-1][1]-prices[i])
        #             dp[i][3] = max(dp[i-1][3], dp[i-1][2]+prices[i])
        :param k:
        :param prices:
        :return:
        """
        len_price = len(prices)

        # j = 0-k
        # 2*j:buy 2*j+1:sell
        dp = [[0] * 2 * k for _ in range(len(prices))]
        for i in range(k):
            dp[0][2 * i] = -prices[0]

        for i in range(1, len_price):
            for j in range(k):
                # buy
                if j == 0:
                    # 第i天进行第0次买
                    dp[i][0] = max(dp[i-1][0], -prices[i])
                else:
                    # 第i天进行第j次买
                    dp[i][2 * j] = max(dp[i-1][2 * j], dp[i-1][2*j-1] - prices[i])

                # sell # 第i天进行第j次卖
                dp[i][2 * j + 1] = max(dp[i-1][2 * j + 1], dp[i-1][2 * j] + prices[i])

        return dp[-1][-1]

