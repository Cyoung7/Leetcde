#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 7_1005. Maximize Sum Of Array After K Negations.py
@time: 2025/4/22 下午2:15
@desc:
"""
import math
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        """
        先排序，有负数先翻负数，没有负数翻绝对值最小的那个数
        :param nums:
        :param k:
        :return:
        """
        nums.sort()
        abs_min = math.inf
        num_idx = 0
        for i in range(k):
            if nums[num_idx] < 0:
                nums[num_idx] = -nums[num_idx]
                abs_min = min(abs_min, abs(nums[num_idx]))
                if num_idx < len(nums)-1:
                    num_idx += 1
            elif 0 <= nums[num_idx] <= abs_min:
                abs_min = min(abs_min, abs(nums[num_idx]))
                nums[num_idx] = -nums[num_idx]
            elif nums[num_idx] > abs_min:
                num_idx -= 1
                nums[num_idx] = -nums[num_idx]

        return sum(nums)

class Solution1:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        """
        先排序，有负数先翻负数，没有负数翻绝对值最小的那个数
        :param nums:
        :param k:
        :return:
        """
        nums.sort(key=lambda x: -abs(x))

        for i in range(len(nums)):
            if nums[i] < 0 < k:
                nums[i] = -nums[i]
                k -= 1
        if k % 2 == 1:
            nums[-1] = - nums[-1]

        return sum(nums)


if __name__ == '__main__':
    s = Solution1()

    print(s.largestSumAfterKNegations([-4,-2,-3], 4))