#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 12_84. Largest Rectangle in Histogram.py
@time: 2025/4/27 上午10:36
@desc:
"""
from typing import List


# 单调栈精简
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        这道题的本质是找到下一个比当前值更小的坐标
        思想就是单调栈:从栈头到栈底单调递减
        单调栈不仅能找到右边第一个比它小的元素
        从栈头到栈底，相邻两个元素也是左边第一个比他小的元素
        :param heights:
        :return:
        """
        heights.insert(0, 0)
        heights.append(0)
        stack = [0]
        result = 0
        for i in range(1, len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                mid_height = heights[stack[-1]]
                stack.pop()
                if stack:
                    # area = width * height
                    area = (i - stack[-1] - 1) * mid_height
                    result = max(area, result)
            stack.append(i)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea([2,1,2]))