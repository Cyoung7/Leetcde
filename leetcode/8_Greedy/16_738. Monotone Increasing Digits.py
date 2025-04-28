#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 16_738. Monotone Increasing Digits.py
@time: 2025/4/22 下午9:19
@desc:
"""


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n == 0:
            return 0

        list_n = list()
        while n > 0:
            list_n.append(n % 10)
            n = int(n / 10)

        result = list()
        result.append(list_n[0])

        for i in range(1, len(list_n)):
            # 出现非递增，后面全部变成9，本位子减1
            if list_n[i] > list_n[i-1]:
                while len(result) > 0 and result[-1] != 9:
                    result.pop()
                while len(result) < i:
                    result.append(9)
                list_n[i] -= 1
                result.append(list_n[i])
            else:
                result.append(list_n[i])

        num = 0
        for i in result[::-1]:
            num = num * 10 + i
        return num


class Solution1:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n == 0:
            return 0

        list_n = list()
        while n > 0:
            list_n.append(n % 10)
            n = int(n / 10)

        flag = 0
        for i in range(1, len(list_n)):
            # 标记最后一个非递增数字
            if list_n[i] > list_n[i-1]:
                flag = i
                list_n[i] -= 1

        for i in range(flag):
            list_n[i] = 9
        num = 0
        for i in list_n[::-1]:
            num = num * 10 + i
        return num

if __name__ == '__main__':
    s = Solution1()
    print(s.monotoneIncreasingDigits(332))

