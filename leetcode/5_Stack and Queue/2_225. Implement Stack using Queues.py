#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 2_225. Implement Stack using Queues.py
@time: 2025/4/12 上午9:14
@desc:
"""
from collections import deque


class MyStack:
    """
    题目：用队列实现栈
    和栈实现队列还是有区别：
    队列实现栈：两个队列,两个队列并不会反转顺序，所以另一个队列是用来备份
    栈实现队列：两个队列实现顺序反转，即可实现队列的先进先出
    """
    def __init__(self):
        # flag可以有效降低备份的数量
        self.flag = 0
        self.one = deque()
        self.two = deque()

    def push(self, x: int) -> None:
        if self.flag % 2 == 0:
            self.one.append(x)
        else:
            self.two.append(x)

    def pop(self) -> int:
        if self.flag % 2 == 0 and len(self.one) == 0:
            self.flag += 1
        elif self.flag % 2 == 1 and len(self.two) == 0:
            self.flag += 1

        if self.flag % 2 == 0:
            while len(self.one) > 1:
                self.two.append(self.one.popleft())
            return self.one.pop()
        else:
            while len(self.two) > 1:
                self.one.append(self.two.popleft())
            return self.two.pop()

    def top(self) -> int:
        top_v = self.pop()
        self.push(top_v)
        return top_v

    def empty(self) -> bool:
        return len(self.one) == 0 and len(self.two) == 0


# Your MyStack object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
