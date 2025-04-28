#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 4_1047. Remove All Adjacent Duplicates In String.py
@time: 2025/4/12 上午10:13
@desc:
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        核心思想：直接用栈实现相同字符的消除
        :param s:
        :return:
        """
        stack = list()
        for c in s:
            if len(stack) == 0:
                stack.append(c)
                continue
            if c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


if __name__ == '__main__':
    s = Solution()