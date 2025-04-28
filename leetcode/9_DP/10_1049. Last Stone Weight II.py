#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 10_1049. Last Stone Weight II.py
@time: 2025/4/23 下午2:42
@desc:
"""
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_stone = sum(stones)
        target = int(sum_stone / 2)

        dp = [0] * (target+1)
        for stone in stones:
            for i in range(target, stone-1, -1):
                dp[i] = max(dp[i], dp[i-stone]+stone)

        return sum_stone - 2 * dp[target]

