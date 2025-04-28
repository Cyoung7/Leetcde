#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 35_392. Is Subsequence.py
@time: 2025/4/25 上午11:51
@desc:
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        朴素的解法:双指针
        :param s:
        :param t:
        :return:
        """
        s_len = len(s)
        if s_len == 0:
            return True

        s_idx = 0
        for i in range(0, len(t)):
            if s[s_idx] == t[i]:
                s_idx += 1
            if s_idx == s_len:
                return True
        return False


class Solution1:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        dp: 编辑举例的入门题
        :param s:
        :param t:
        :return:
        """
        if len(s) == 0:
            return True
        # dp[i][j] 表示以下标i-1为结尾的字符串s，和以下标j-1为结尾的字符串t，相同子序列的长度为dp[i][j]。
        dp = [[0] * (len(s)+1) for _ in range(len(t)+1)]
        len_s = len(s)
        for i in range(1, len(t)+1):
            for j in range(1, len(s)+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # 这道题和1143最大的区别
                    # 1143可以两个序列都可以剔除:dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    # 本题是只其中一个序列剔除
                    dp[i][j] = dp[i-1][j]
                if dp[i][j] == len_s:
                    return True
        return False
