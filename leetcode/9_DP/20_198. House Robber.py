#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 20_198. House Robber.py
@time: 2025/4/24 上午11:38
@desc:
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        len_num = len(nums)
        # dp[i]:前i间房偷盗的最大金额
        dp = [0] * (len_num+1)

        for i in range(1, len_num+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        return dp[len_num]