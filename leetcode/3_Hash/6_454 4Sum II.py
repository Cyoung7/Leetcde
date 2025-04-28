#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 6_454 4Sum II.py
@time: 2025/4/9 上午11:34
@desc:
"""
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        核心思想：利用hash结构存储前两个数组结果
        :param nums1:
        :param nums2:
        :param nums3:
        :param nums4:
        :return:
        """
        pre_sum = dict()
        for num1 in nums1:
            for num2 in nums2:
                if pre_sum.get(num1 + num2) is None:
                    pre_sum[num1 + num2] = 1
                else:
                    pre_sum[num1 + num2] += 1
        count = 0
        for num3 in nums3:
            for num4 in nums4:
                if pre_sum.get(0 - (num3 + num4)) is not None:
                    count += pre_sum[0 - (num3 + num4)]
        return count


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    s.fourSumCount(nums1, nums2, nums3, nums4)
