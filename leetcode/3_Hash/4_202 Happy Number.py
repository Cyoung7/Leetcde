#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 4_202 Happy Number.py
@time: 2025/4/9 上午10:26
@desc:
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        """
        核心思想：sum会重复出现, 用hash记录sum结果
        :param n:
        :return:
        """
        tmp_num = n
        result = set()
        while tmp_num != 1:
            sec_num = 0
            while tmp_num:
                sec_num += ((tmp_num % 10) ** 2)
                tmp_num = int(tmp_num / 10)

            if sec_num in result:
                return False

            result.add(sec_num)
            tmp_num = sec_num

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(19))