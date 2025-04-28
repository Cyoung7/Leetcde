#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 17_322. Coin Change.py
@time: 2025/4/24 上午10:10
@desc:
"""
import math
import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        # 这里由于推导式求min，所以初始化最大值
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0

        # 这里是完全背包，只是求最小个数，并不是求组合数和排列数，所以遍历顺序都可以
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == sys.maxsize:
            return -1
        return dp[amount]


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([186,419,83,408], 6249))