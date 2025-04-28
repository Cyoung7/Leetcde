#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 1_232. Implement Queue using Stacks.py
@time: 2025/4/12 上午9:00
@desc:
"""


class MyQueue:
    """
    题目：用栈实现队列
    核心思想：两个栈，一个用于进，一个用于出
    """
    def __init__(self):
        self.in_list = list()
        self.out_list = list()

    def push(self, x: int) -> None:
        self.in_list.append(x)

    def pop(self) -> int:
        if len(self.out_list) == 0:
            while len(self.in_list) > 0:
                self.out_list.append(self.in_list.pop())
        return self.out_list.pop()

    def peek(self) -> int:
        if len(self.out_list) == 0:
            while len(self.in_list) > 0:
                self.out_list.append(self.in_list.pop())
        return self.out_list[-1]

    def empty(self) -> bool:
        return len(self.in_list) == 0 and len(self.out_list) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

if __name__ == '__main__':
    pass