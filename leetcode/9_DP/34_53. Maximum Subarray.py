#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 34_53. Maximum Subarray.py
@time: 2025/4/25 上午11:35
@desc:
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        之前是用贪心做的，现在用dp做
        :param nums:
        :return:
        """
        # dp[i]:包括下标i（以nums[i]为结尾）的最大连续子序列和为dp[i]。
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)

