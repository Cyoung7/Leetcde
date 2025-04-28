#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 8_739. Daily Temperatures.py
@time: 2025/4/25 下午5:14
@desc: 单调栈1
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = list()
        # if len(temperatures) > 0:
        #     stack.append(temperatures[0])
        for i in range(0, len(temperatures)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                top_i = stack.pop()
                results[top_i] = i - top_i
            stack.append(i)
        return results

