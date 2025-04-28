#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 9_496. Next Greater Element I.py
@time: 2025/4/25 下午5:32
@desc:单调栈
"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        results = [-1] * len(nums1)
        # num1中数值到idx的映射
        map_idx = dict()
        for i in range(len(nums1)):
            map_idx[nums1[i]] = i

        stack = list()
        for i in range(len(nums2)):
            while len(stack) > 0 and nums2[i] > nums2[stack[-1]]:
                top_i = stack.pop()
                # nums2[top_i]是否再num1中
                if map_idx.get(nums2[top_i]) is not None:
                    # map_idx[nums2[top_i]]: 取出数在num1中的下标
                    results[map_idx[nums2[top_i]]] = nums2[i]
            stack.append(i)
        return results
