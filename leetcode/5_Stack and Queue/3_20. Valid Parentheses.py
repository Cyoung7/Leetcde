#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 3_20. Valid Parentheses.py
@time: 2025/4/12 上午10:02
@desc:
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        核心思想：直接用栈实现括号的匹配
        :param s:
        :return:
        """
        stack = list()

        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
                continue
            if c in [")", "}", "]"] and len(stack) == 0:
                return False

            if c == ")":
                if stack.pop() != "(":
                    return False
            elif c == "}":
                if stack.pop() != "{":
                    return False
            elif c == "]":
                if stack.pop() != "[":
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()[]{}"))