#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 12_452. Minimum Number of Arrows to Burst Balloons.py
@time: 2025/4/22 下午5:17
@desc:
"""
from typing import List


class Solution:

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        核心思想：能一起射爆的气球，他们的共同边界越来越小
        :param points:
        :return:
        """
        points.sort(key=lambda x: x[0])
        results = 1
        bound = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > bound:
                results += 1
                bound = points[i][1]
            else:
                # 贪心，找最近共同边界
                bound = min(points[i][1], bound)
        return results


if __name__ == '__main__':
    s = Solution()
    print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))