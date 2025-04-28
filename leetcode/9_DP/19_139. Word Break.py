#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 19_139. Word Break.py
@time: 2025/4/24 上午10:59
@desc:
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        len_s = len(s)
        dp = [False for _ in range(len_s + 1)]
        dp[0] = True

        # 本质是一个完全背包的排列问题，所以需要先遍历容量，后遍历单词表
        for i in range(1, len_s+1):
            for word in wordDict:
                len_w = len(word)
                if i >= len_w:
                    sub_s = s[i-len_w: i]
                    if sub_s == word:
                        dp[i] = dp[i] or dp[i-len_w]
        return dp[len_s]
