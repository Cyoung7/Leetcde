#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 6_45. Jump Game II.py
@time: 2025/4/22 下午1:42
@desc:
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        核心思想：前面子数组需要到达的最小步骤
        真难：想到思想，代码都不一定写得出来
        :param nums:
        :return:
        """
        if len(nums) <= 1:
            return 0
        len_num = len(nums)
        step = 0
        next_distance = 0
        cur_distance = 0
        for i in range(len_num):
            # 截至i，能走到下一个最大的范围就是next_distance
            next_distance = max(next_distance, i + nums[i])
            if i == cur_distance:
                step += 1
                cur_distance = next_distance
            if cur_distance >= len_num-1:
                break
        return step

