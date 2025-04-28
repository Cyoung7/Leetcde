#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 8_78. Subsets.py
@time: 2025/4/18 上午11:25
@desc:
"""
import copy
from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = list()
        path_result = list()

        def dfs(tmp_nums: List[int]):
            results.append(copy.copy(path_result))
            # if len(tmp_nums) == 0:
            #     return
            for i in range(len(tmp_nums)):
                path_result.append(tmp_nums[i])
                dfs(tmp_nums[i + 1:])
                path_result.pop()
            return

        dfs(nums)
        return results


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))
