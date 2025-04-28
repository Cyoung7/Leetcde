#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 15_56. Merge Intervals.py
@time: 2025/4/22 下午8:45
@desc:
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        刷到这里，终于有点贪心的感觉了
        :param intervals:
        :return:
        """
        intervals.sort(key=lambda x: x[0])

        result = list()
        start = intervals[0][0]
        bound = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > bound:
                result.append([start, bound])
                start = intervals[i][0]
                bound = intervals[i][1]
            else:
                # 贪心，找最远边界
                bound = max(bound, intervals[i][1])
        result.append([start, bound])
        return result
