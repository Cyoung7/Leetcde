#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 1_77. Combinations.py
@time: 2025/4/17 下午5:08
@desc:
"""
import copy
from typing import List


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        几年没写回溯算法，还是跌跌幢幢撸出来了
        :param n:
        :param k:
        :return:
        """
        results = list()
        path = list()

        def back_tracking(start: int, end: int):
            nonlocal k, path
            if len(path) == k:
                results.append(copy.copy(path))
                return
            for i in range(start, end):
                # 剪枝, 不剪不影响结果，只是稍慢
                if i + (k - len(path)) > end:
                    break
                path.append(i)
                back_tracking(i + 1, end)
                path.pop()
            return

        back_tracking(1, n + 1)
        return results


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
