#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 14_518. Coin Change II.py
@time: 2025/4/23 下午3:53
@desc:
"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]


class Solution1:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins))]

        for j in range(amount + 1):
            if j % coins[0] == 0:
                dp[0][j] = 1

        for i in range(1, len(coins)):
            for j in range(0, amount + 1):
                if j < coins[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    # dp[i][j - coins[i]]
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]]
        return dp[-1][amount]


if __name__ == '__main__':
    s = Solution1()
    print(s.change(5, [1, 2, 5]))
