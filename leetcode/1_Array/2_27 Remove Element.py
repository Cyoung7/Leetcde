#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 2_27.py
@time: 2025/4/1 上午10:32
@desc:
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        核心思想：双向指针
        :param nums:
        :param val:
        :return:
        """
        start = 0
        end = len(nums)-1
        while start <= end:
            while nums[start] != val:
                start += 1
                if start > end:
                    break
            if start > end:
                break
            while nums[end] == val and end >= 0:
                end -= 1

            if end > start:
                nums[start] = nums[end]
                start += 1
                end -= 1
        return start


if __name__ == '__main__':
    s = Solution()
    nums = [1]
    val = 1
    print(s.removeElement(nums, val))
    print(nums)