#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 11_46. Permutations.py
@time: 2025/4/18 下午1:48
@desc:
"""
import copy
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = list()
        path_result = list()

        def dfs(sub_num: List[int]):
            if len(sub_num) == 0:
                results.append(copy.copy(path_result))
                return
            for i in range(len(sub_num)):
                path_result.append(sub_num[i])
                # 全排列和前面组合，分割的最大区别在于 集合前面用过的，下一层不会再用，
                # 而全排列下一层需要用到上一次之前用过的元素
                new_nums = sub_num[:i] + sub_num[i + 1:]
                dfs(new_nums)
                path_result.pop()
            return

        dfs(nums)
        return results


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
