#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 1_704.py
@time: 2025/4/1 上午9:48
@desc:
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        核心思想：
        二分查找前提条件：1.有序数组。2.数组元素没有重复
        :param nums:
        :param target:
        :return:
        """
        start = 0
        end = len(nums) - 1
        while start <= end:  # 这里end是len(nums) - 1，所以是左闭右闭区间用 <= ,如果是左闭右开区间就用 <
            mid = int((start+end) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    # nums = [-1, 0, 3, 5, 9, 12]
    # target = 2
    print(s.search(nums, target))