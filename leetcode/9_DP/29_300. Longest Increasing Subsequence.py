#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 29_300. Longest Increasing Subsequence.py
@time: 2025/4/25 上午9:25
@desc:
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i]表示i之前包括i的 **[以nums[i]结尾] 的最长递增子序列的长度
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
