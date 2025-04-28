#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 23_121. Best Time to Buy and Sell Stock.py
@time: 2025/4/24 下午1:38
@desc:
"""
import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        122. Best Time to Buy and Sell Stock II 在贪心的分类下，也有递归解法
        这里用双指针解决
        :param prices:
        :return:
        """
        low_point = prices[0]
        max_diff = 0

        for i in range(1, len(prices)):
            fast_point = prices[i]
            # 一旦后面出现了最低值，前面低点的值就失去了锚点意义
            if fast_point < low_point:
                low_point = fast_point
                continue
            if fast_point - low_point > max_diff:
                max_diff = fast_point - low_point
        return max_diff


class Solution1:
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
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], prices[i] + dp[i-1][0])
        return dp[-1][1]


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp
        :param prices:
        :return:
        """
        # dp[i][0]持有股票 手中的现金   dp[i][1]不持有股票 手中的现金
        dp = [0, 0]
        dp[0] = -prices[0]
        dp[1] = 0

        for i in range(1, len(prices)):
            dp[1] = max(dp[1], prices[i] + dp[0])
            dp[0] = max(dp[0], -prices[i])

        return dp[1]


if __name__ == '__main__':
    s = Solution1()
    print(s.maxProfit([7,6,4,3,1]))