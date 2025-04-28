#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 4_Right Rotate Str.py
@time: 2025/4/10 上午11:38
@desc:
题目链接
https://kamacoder.com/problempage.php?pid=1065
55. 右旋字符串（第八期模拟笔试）
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> List[str]:
        """
        核心思想：双指针法，不仅能节约时间复杂度，还能节约空间复杂度
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            tmp, s[left] = s[left], s[right]
            s[right] = tmp
            left += 1
            right -= 1
        return s

    def rightRotateStr(self, s: str, k: int) -> str:
        """
        核心思想：取出末尾k个元素反转，拼接前len-k个元素
        :param s:
        :param k:
        :return:
        """
        r_s = s[len(s)-k:]
        r_list = self.reverseString([r_s[i] for i in range(k)])
        return "{}{}".format("".join(r_list), s[:len(s)-k])


if __name__ == '__main__':
    s = Solution()
    print(s.rightRotateStr("abcdefg", 2))