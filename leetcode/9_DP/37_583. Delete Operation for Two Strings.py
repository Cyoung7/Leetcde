#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 37_583. Delete Operation for Two Strings.py
@time: 2025/4/25 下午1:36
@desc:
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        就是1143最长公共子序列的变种
        :param word1:
        :param word2:
        :return:
        """
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word2[j-1] == word1[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return len(word1) + len(word2) - 2 * dp[-1][-1]


class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        :param word1:
        :param word2:
        :return:
        """
        # dp[i][j]：以i-1为结尾的字符串word1，和以j-1位结尾的字符串word2，想要达到相等，所需要删除元素的最少次数。
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        # init
        for i in range(0, len(word1) + 1):
            dp[i][0] = i
        for j in range(0, len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word2[j-1] == word1[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[-1][-1]
