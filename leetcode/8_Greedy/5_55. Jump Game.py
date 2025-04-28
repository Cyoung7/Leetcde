#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 5_55. Jump Game.py
@time: 2025/4/22 下午1:03
@desc:
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        这道题是贪心的典型
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return True
        next_distance = 0
        len_num = len(nums)
        # 核心思想：贪心，挨着遍历，求局部最大值
        for i in range(len_num):
            # 说明cover都走不到i
            if i > next_distance:
                return False
            next_distance = max(i + nums[i], next_distance)
            if next_distance >= len_num - 1:
                return True
        return False
