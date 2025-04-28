#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 1_455. Assign Cookies.py
@time: 2025/4/22 上午10:45
@desc:
"""
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """

        :param g: child
        :param s: cookie
        :return:
        """
        len_g = len(g)
        len_s = len(s)
        g.sort()
        s.sort()
        # 截取最小数组的长度
        min_len = len_s
        if len_g > len_s:
            g = g[:len_s]
        elif len_s > len_g:
            s = s[len_s-len_g:]
            min_len = len_g

        result = 0
        # 尽量让大的饼干满足大的孩子
        s_idx = min_len-1
        # 从大到小遍历孩子，如果从小到达，就是遍历饼干
        for i in range(min_len-1, -1, -1):
            if s[s_idx] >= g[i]:
                s_idx -= 1
                result += 1
        return result


if __name__ == '__main__':

    for i in range(5, 1, -1):
        print(i)