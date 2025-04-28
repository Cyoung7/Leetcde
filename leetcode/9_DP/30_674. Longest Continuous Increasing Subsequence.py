#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 30_674. Longest Continuous Increasing Subsequence.py
@time: 2025/4/25 上午9:46
@desc:
"""
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        dp
        :param nums:
        :return:
        """
        # dp[i]表示i之前包括i的 **[以nums[i]结尾] 的最长连续递增子序列的长度
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
        return max(dp)


class Solution1:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        贪心
        :param nums:
        :return:
        """
        result = 1
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur += 1
            else:
                cur = 1
            # 贪心
            if cur > result:
                result = cur
        return result
