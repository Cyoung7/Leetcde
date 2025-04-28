#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 39_647. Palindromic Substrings.py
@time: 2025/4/25 下午2:44
@desc:
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        这个题不刷也是不容易想到的，dp数组的定义和其他不同
        :param s:
        :return:
        """
        # 布尔类型的dp[i][j]：表示区间范围[i,j] （注意是左闭右闭）的子串是否是回文子串，如果是dp[i][j]为true，否则为false。
        dp = [[False] * (len(s)) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if i+1 == j:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
        return sum([x for row in dp for x in row])


class Solution1:
    def countSubstrings(self, s: str) -> int:
        """
        这个双指针也不太好想
        :param s:
        :return:
        """
        result = 0
        for i in range(len(s)):
            result += self.extend(s, i, i, len(s))  # 以i为中心
            result += self.extend(s, i, i + 1, len(s))  # 以i和i+1为中心
        return result

    def extend(self, s, i, j, n):
        res = 0
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1
            res += 1
        return res
