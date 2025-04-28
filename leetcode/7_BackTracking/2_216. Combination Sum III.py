#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 2_216. Combination Sum III.py
@time: 2025/4/18 上午8:55
@desc:
"""
import copy
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        results = list()
        path_value = list()

        def dfs(tmp_n, tmp_k, start):
            nonlocal path_value, results, k, n
            # 简单的剪枝
            if tmp_n > n:
                return

            if tmp_k >= k:
                if tmp_n == n:
                    results.append(copy.copy(path_value))
                return

            for i in range(start, 10):
                path_value.append(i)
                dfs(tmp_n+i, tmp_k+1, i+1)
                path_value.pop()
            return
        dfs(0, 0, 1)
        return results
