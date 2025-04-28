#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 10_503. Next Greater Element II.py
@time: 2025/4/25 下午5:46
@desc:
"""
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        results = [-1] * len(nums)

        stack = list()
        # 第一遍遍历
        for i in range(len(nums)):
            while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                top_i = stack.pop()
                results[top_i] = nums[i]
            stack.append(i)
        # 第二遍遍历
        for i in range(len(nums)):
            while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                top_i = stack.pop()
                results[top_i] = nums[i]
            # 经历第一次遍历后，最大数一定在最下面，
            # 只剩下最大数时，即可结束
            # if len(stack) <= 1:
            #     break
            # 第二次已经不需要在入栈了
            # stack.append(i)
        return results
