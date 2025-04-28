#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 10_491. Non-decreasing Subsequences.py
@time: 2025/4/18 下午1:22
@desc:
"""
import copy
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """
        这道题的重点是没法排序去重，所以需要一个set集合记录本层使用过的元素去重
        :param nums:
        :return:
        """
        results = list()
        tmp_result = list()

        def dfs(sub_nums: List[int]):
            if len(tmp_result) > 1:
                results.append(copy.copy(tmp_result))

            # 本层去重
            record_set = set()
            for i in range(len(sub_nums)):
                # 上一层与下一层的去重
                if len(tmp_result) > 0 and sub_nums[i] < tmp_result[-1]:
                    continue
                # 本层去重
                if sub_nums[i] in record_set:
                    continue
                record_set.add(sub_nums[i])
                tmp_result.append(sub_nums[i])
                dfs(sub_nums[i + 1:])
                tmp_result.pop()

        dfs(nums)
        return results


class Solution1:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        results = list()
        tmp_result = list()

        def dfs(sub_nums: List[int]):
            if len(tmp_result) > 1:
                results.append(copy.copy(tmp_result))

            # 本层去重
            record_set = [0 for i in range(200)]

            for i in range(len(sub_nums)):
                # 上一层与下一层的去重
                if len(tmp_result) > 0 and sub_nums[i] < tmp_result[-1]:
                    continue
                # 本层去重
                if record_set[sub_nums[i] + 100] == 1:
                    continue
                record_set[sub_nums[i] + 100] = 1
                tmp_result.append(sub_nums[i])
                dfs(sub_nums[i + 1:])
                tmp_result.pop()

        dfs(nums)
        return results


if __name__ == '__main__':
    s = Solution1()
    print(s.findSubsequences([4, 6, 7, 7]))
