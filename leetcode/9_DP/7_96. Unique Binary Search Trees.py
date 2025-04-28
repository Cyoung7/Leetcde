#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 7_96. Unique Binary Search Trees.py
@time: 2025/4/23 下午12:20
@desc:
"""


class Solution:
    def numTrees(self, n: int) -> int:
        """
        太难了
        dp[3]，就是 元素1为头结点搜索树的数量 + 元素2为头结点搜索树的数量 + 元素3为头结点搜索树的数量
        元素1为头结点搜索树的数量 = 右子树有2个元素的搜索树数量 * 左子树有0个元素的搜索树数量
        元素2为头结点搜索树的数量 = 右子树有1个元素的搜索树数量 * 左子树有1个元素的搜索树数量
        元素3为头结点搜索树的数量 = 右子树有0个元素的搜索树数量 * 左子树有2个元素的搜索树数量
        有2个元素的搜索树数量就是dp[2]。
        有1个元素的搜索树数量就是dp[1]。
        有0个元素的搜索树数量就是dp[0]。
        所以dp[3] = dp[2] * dp[0] + dp[1] * dp[1] + dp[0] * dp[2]
        :param n:
        :return:
        """
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n + 1):
            # dp[i]的状态转移函数
            # 元素头节点为j
            for j in range(1, i+1):
                dp[i] += dp[i-j] * dp[j-1]
        return dp[n]
