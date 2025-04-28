#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 5_150. Evaluate Reverse Polish Notation.py
@time: 2025/4/12 上午10:32
@desc:
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        核心思想：用栈记录操作数，代码没有检查逆波兰表达式的有效性
        :param tokens:
        :return:
        """

        stack = list()

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
            if token in ["+", "-", "*", "/"]:
                right = stack.pop()
                left = stack.pop()

                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                elif token == "/":
                    stack.append(int(left / right))

        return stack[0]


if __name__ == '__main__':
    s = Solution()
