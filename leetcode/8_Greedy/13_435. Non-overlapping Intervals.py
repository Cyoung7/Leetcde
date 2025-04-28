#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 13_435. Non-overlapping Intervals.py
@time: 2025/4/22 下午5:43
@desc:
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        remove = 0
        cur_bound = intervals[0][1]

        for i in range(1, len(intervals)):
            # 重叠处理
            if cur_bound > intervals[i][0]:
                # 保留bound边界小的,以至于后面的更不容易重叠
                cur_bound = min(cur_bound, intervals[i][1])
                remove += 1
            else:
                cur_bound = intervals[i][1]
        return remove


if __name__ == '__main__':
    s = Solution()
    print(s.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))