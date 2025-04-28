#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 3_977 Squares of a Sorted Array.py
@time: 2025/4/1 下午1:27
@desc:
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        核心思想：双向指针
        必须新开数组存放结果，不能交换原数组成员的位置，交换以后完全就乱序了
        :param nums:
        :return:
        """
        new_nums = [0 for i in range(len(nums))]
        start = 0
        end = len(nums) - 1
        new_end = end
        while start <= end:
            if abs(nums[start]) >= abs(nums[end]):
                new_nums[new_end] = nums[start] * nums[start]
                start += 1
            else:
                new_nums[new_end] = nums[end] * nums[end]
                end -= 1
            new_end -= 1
        return new_nums


if __name__ == '__main__':
    s = Solution()
    # nums = [-5,-3,-2,-1]
    nums = [-4,-1,0,3,10]
    print(s.sortedSquares(nums))