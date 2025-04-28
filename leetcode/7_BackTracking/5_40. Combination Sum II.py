#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 5_40. Combination Sum II.py
@time: 2025/4/18 上午10:01
@desc:
"""
import copy
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = list()
        path_value = list()

        def dfs(tmp_candidates, tmp_target):
            nonlocal target, path_value, results

            if tmp_target == target:
                results.append(copy.copy(path_value))
                return
            # 有序的情况下，剪枝更多, 无序判断: tmp_target > target
            if len(tmp_candidates) == 0 or tmp_target + tmp_candidates[0] > target:
                return

            for i in range(len(tmp_candidates)):
                # 这里处理是关键，同一层，两个相同的数字不能重复用，重复用就有重复的结果
                # 保证了同一层不使用相同数字，就不会有重复的结果
                if i > 0:
                    if tmp_candidates[i] == tmp_candidates[i-1]:
                        continue
                path_value.append(tmp_candidates[i])
                dfs(tmp_candidates[i + 1:], tmp_target + tmp_candidates[i])
                path_value.pop()
            return

        # 先排序更有利于剪枝
        candidates = sorted(candidates)
        dfs(candidates, 0)
        return results


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
