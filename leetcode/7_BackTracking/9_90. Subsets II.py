#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 9_90. Subsets II.py
@time: 2025/4/18 下午1:15
@desc:
"""
import copy
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = list()
        path_result = list()

        def dfs(tmp_nums: List[int]):
            results.append(copy.copy(path_result))

            for i in range(len(tmp_nums)):
                # 这里做本层去重处理
                if i > 0 and tmp_nums[i] == tmp_nums[i-1]:
                    continue
                path_result.append(tmp_nums[i])
                dfs(tmp_nums[i + 1:])
                path_result.pop()
            return
        # 排序+去重，常规操作
        nums = sorted(nums)
        dfs(nums)
        return results


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2]))
