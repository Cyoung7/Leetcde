#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 8_134. Gas Station.py
@time: 2025/4/22 下午3:41
@desc:
"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        sum_diff = 0
        cur_diff = 0
        start = 0

        for i in range(len(gas)):
            sum_diff += (gas[i] - cost[i])
            cur_diff += (gas[i] - cost[i])
            # 那么局部最优：当前累加rest[i]的和cur_diff一旦小于0，起始位置至少要是i+1，因为从i之前开始一定不行。全局最优：找到可以跑一圈的起始位置
            if cur_diff < 0:
                start = i + 1
                cur_diff = 0
        # 遍历一遍，总的油够，总能找到一个起始位置的
        if sum_diff < 0:
            return -1
        return start
