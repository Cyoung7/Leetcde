#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 5_1 Two Sum.py
@time: 2025/4/9 上午11:09
@desc:
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        核心思想：利用hash结构存储索引结果
        什么时候使用哈希法? 当我们需要查询一个元素是否出现过，或者一个元素是否在集合里的时候
        :param nums:
        :param target:
        :return:
        """
        idx_result = dict()
        for idx, num in enumerate(nums):
            if idx_result.get(target-num) is not None:
                return [idx_result[target-num], idx]
            idx_result[num] = idx
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15],9))