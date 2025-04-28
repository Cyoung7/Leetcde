#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 21_213. House Robber II.py
@time: 2025/4/24 上午11:54
@desc:
"""
from typing import List


class Solution:
    def robRange(self, nums: List[int]) -> int:
        len_num = len(nums)
        # dp[i]:前i间房偷盗的最大金额
        dp = [0] * (len_num+1)

        for i in range(1, len_num+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        return dp[len_num]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        left = self.robRange(nums[:-1])
        right = self.robRange(nums[1:])
        return max(left, right)