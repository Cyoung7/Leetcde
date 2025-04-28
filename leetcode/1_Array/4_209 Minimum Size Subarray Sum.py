#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 4_209 Minimum Size Subarray Sum.py
@time: 2025/4/1 下午2:23
@desc:
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        核心思想：滑动窗口, for循环表示滑动窗口的结束位置
        在本题中实现滑动窗口，主要确定如下三点：
            窗口内是什么？
            如何移动窗口的起始位置？
            如何移动窗口的结束位置
        :param target:
        :param nums:
        :return:
        """
        min_len = 0

        start = 0
        end = 0
        length = len(nums)

        sub_sum = 0
        while end < length:
            sub_sum += nums[end]
            end += 1

            while sub_sum - nums[start] >= target:
                sub_sum -= nums[start]
                start += 1

            if sub_sum >= target:
                if min_len == 0 or min_len > end - start:
                    min_len = end - start

        return min_len


if __name__ == '__main__':
    s = Solution()
    target = 7
    nums = [2,3,1,2,4,3]
    print(s.minSubArrayLen(target,nums))