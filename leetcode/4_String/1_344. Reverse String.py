#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 1_344. Reverse String.py
@time: 2025/4/10 上午9:44
@desc:
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        核心思想：双指针法，不仅能节约时间复杂度，还能节约空间复杂度
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            s[right], s[left] = s[left], s[right]
            left += 1
            right -= 1


if __name__ == '__main__':
    s = Solution()
    s.reverseString(["h", "e", "l", "l", "o"])
