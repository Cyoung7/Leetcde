#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 33_1035. Uncrossed Lines.py
@time: 2025/4/25 上午11:17
@desc:
"""
from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
        和1143本质是一道完全相同的题
        :param nums1:
        :param nums2:
        :return:
        """
        # dp[i][j]nums1[0:i-1] 与 nums2[0:j-1] 的最长子序列长度
        dp = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)]

        result = 0
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

                if dp[i][j] > result:
                    result = dp[i][j]
        return result
