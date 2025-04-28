#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 11_42. Trapping Rain Water.py
@time: 2025/4/27 上午9:58
@desc:
"""
from typing import List


# 单调栈压缩版
class Solution:
    """
    这道题用单调栈太抽象了，需要多练习
    栈顶存在高度相同的元素，计算出来的高度差为0，所以不影响结果
    """
    def trap(self, height: List[int]) -> int:
        stack = [height[0]]
        result = 0
        for i in range(1, len(height)):
            while stack and height[i] > height[stack[-1]]:
                mid_height = stack.pop()
                if stack:
                    # 雨水高度是 min(凹槽左侧高度, 凹槽右侧高度) - 凹槽底部高度
                    h = min(height[stack[-1]], height[i]) - height[mid_height]
                    # 雨水宽度是 凹槽右侧的下标 - 凹槽左侧的下标 - 1
                    w = i - stack[-1] - 1
                    # 累计总雨水体积
                    result += h * w
            stack.append(i)
        return result


class Solution1:
    """
    自己写还是优先双指针
    """
    def trap(self, height: List[int]) -> int:
        lh = [0] * len(height)
        rh = [0] * len(height)

        lh[0] = height[0]
        for i in range(1, len(height)):
            lh[i] = max(lh[i-1], height[i])
        rh[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            rh[i] = max(rh[i+1], height[i])
        sum_rain = 0
        for i in range(1, len(height)-1):
            h = min(lh[i], rh[i]) - height[i]
            sum_rain += h
        return sum_rain


if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))