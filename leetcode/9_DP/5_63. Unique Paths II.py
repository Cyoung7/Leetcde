#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 5_63. Unique Paths II.py
@time: 2025/4/23 上午11:19
@desc:
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        这里的主要难点是初始化问题，
        边界的初始化，只要遇到障碍物，直接后面都是0了，
        而不是只有障碍物的地方初始化0
        :param obstacleGrid:
        :return:
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # dp[i][j]标识到达i,j坐标有多少种走法
        dp = [[0]*n for _ in range(m)]

        # 初始化边界
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            else:
                dp[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            else:
                dp[0][j] = 1
        # 这样就不用处理边界的特殊情况了
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
