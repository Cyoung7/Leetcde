#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 5_28. Find the Index of the First Occurrence in a String.py
@time: 2025/4/10 下午1:40
@desc:
"""
from typing import List


class Solution:
    """
    KMP:这个理解是真复杂
    """
    def getNext(self, next_l: List[int], s: str) -> None:
        j = 0  # j代表前缀末端
        next_l[0] = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                # next_l[j - 1] 代表0到j-1串的前后缀公共串
                # 新j = next_l[j - 1]，0到新j-1的串（新j个字符），一定与i前面的新j个字符是相同的，所以下一次比较从新j的地方开始
                j = next_l[j - 1]
            if s[i] == s[j]:
                j += 1
            next_l[i] = j

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        next_l = [0] * len(needle)
        self.getNext(next_l, needle)

        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next_l[j - 1]

            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    s1 = "mississippi"
    s2 = "aabaaa"
    print(s.strStr(s1, s2))
