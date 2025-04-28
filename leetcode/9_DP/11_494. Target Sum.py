#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 11_494. Target Sum.py
@time: 2025/4/23 下午3:52
@desc:
"""
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        """
        一维dp数组
        :param nums:
        :param target:
        :return:
        """
        sum_nums = sum(nums)
        if abs(target) > sum_nums:
            return 0
        if (sum_nums + target) % 2 != 0:
            return 0

        bag_size = (sum_nums + target) // 2
        dp = [0] * (bag_size + 1)
        dp[0] = 1

        for num in nums:
            for i in range(bag_size, num-1, -1):
                dp[i] += dp[i-num]
        return dp[bag_size]


class Solution1:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        二维dp数组
        :param nums:
        :param target:
        :return:
        """
        sum_nums = sum(nums)
        if abs(target) > sum_nums:
            return 0
        if (sum_nums + target) % 2 != 0:
            return 0

        bag_size = (sum_nums + target) // 2
        dp = [[0] * (bag_size + 1) for _ in range(len(nums))]
        if nums[0] <= bag_size:
            dp[0][nums[0]] = 1
        dp[0][0] = 1

        num_zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                num_zero += 1
            dp[i][0] = 2**num_zero

        for i in range(1, len(nums)):
            for j in range(1, bag_size+1):
                if nums[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]

        return dp[-1][bag_size]
