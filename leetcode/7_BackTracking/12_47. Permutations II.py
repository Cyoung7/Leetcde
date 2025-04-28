#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 12_47. Permutations II.py
@time: 2025/4/18 下午2:01
@desc:
"""
import copy
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = list()
        path_result = list()

        def dfs(sub_num: List[int]):
            if len(sub_num) == 0:
                results.append(copy.copy(path_result))
                return
            for i in range(len(sub_num)):
                # 本题同样多了一个本层去重
                if i > 0 and sub_num[i] == sub_num[i - 1]:
                    continue
                path_result.append(sub_num[i])
                # 全排列和前面组合，分割的最大区别在于 组合，分割的集合前面用过的，下一层不会再用，
                # 而全排列下一层需要用到上一次之前用过的元素
                new_nums = sub_num[:i] + sub_num[i + 1:]
                dfs(new_nums)
                path_result.pop()
            return

        nums = sorted(nums)
        dfs(nums)
        return results


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1, 1, 2]))
