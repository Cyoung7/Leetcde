#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 38_72. Edit Distance.py
@time: 2025/4/25 下午2:06
@desc:
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        这道题根据前面的铺垫，自己写出来的，开心
        :param word1:
        :param word2:
        :return:
        """
        # dp[i][j] 表示以下标i-1为结尾的字符串word1，和以下标j-1为结尾的字符串word2，最近编辑距离为dp[i][j]。
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
                    # 分别对应 删除 插入 替换操作
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
        return dp[-1][-1]
