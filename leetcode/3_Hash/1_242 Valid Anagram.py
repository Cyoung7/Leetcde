#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 1_242 Valid Anagram.py
@time: 2025/4/9 上午9:00
@desc:
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        核心思想：hash表记录每个字符出现的次数
        :param s:
        :param t:
        :return:
        """
        if len(s) != len(t):
            return False
        arr_count = [0 for i in range(26)]

        for i in range(len(s)):
            arr_count[ord(s[i])-97] += 1
            arr_count[ord(t[i]) - 97] -= 1
        return not any(arr_count)


if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram("rat", "nagaram"))