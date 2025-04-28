#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 2_541. Reverse String II.py
@time: 2025/4/10 上午10:00
@desc:
"""
from typing import List


class Solution:
    def reverseSubString(self, s: List[str]) ->  List[str]:
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

    def reverseStr(self, s: str, k: int) -> str:
        s_len = len(s)
        list_s = [s[i] for i in range(s_len)]

        sub_idx = 0
        flag = 0

        while sub_idx < s_len:
            if flag % 2 == 0:
                end_idx = min(sub_idx + k, s_len)
                list_s[sub_idx:end_idx] = self.reverseSubString(list_s[sub_idx:end_idx])
            flag += 1
            sub_idx += k

        return ''.join(list_s)


if __name__ == '__main__':
    s = "abcdefghij"
    k = 4
    obj = Solution()
    print(obj.reverseStr(s, k))
