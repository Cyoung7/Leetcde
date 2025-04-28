#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 3_53. Maximum Subarray.py
@time: 2025/4/22 上午11:48
@desc:
"""
import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        result = -math.inf
        count = 0
        for i in range(0, len(nums)):
            count += nums[i]
            if count > result:
                result = count
            # 只要前面子序列的和大于0；就有保留的意义
            if count < 0:
                count = 0
        return result
