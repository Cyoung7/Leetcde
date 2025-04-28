#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 2_376. Wiggle Subsequence.py
@time: 2025/4/22 上午11:10
@desc:
"""
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            if nums[0] != nums[1]:
                return 2
            else:
                return 1

        result = 0
        pre_diff = nums[1] - nums[0]
        for i in range(2, len(nums)):
            cur_diff = nums[i] - nums[i - 1]
            if pre_diff == 0:
                pre_diff = cur_diff
            elif pre_diff > 0 > cur_diff:
                result += 1
                pre_diff = cur_diff
            elif pre_diff < 0 < cur_diff:
                result += 1
                pre_diff = cur_diff
            elif cur_diff == 0 or (cur_diff > 0 and pre_diff > 0) or (cur_diff < 0 and pre_diff < 0):
                pass
        # 完全相同，端点只记录一个，不相同两边端点都记录
        if result == 0 and nums[0] == nums[-1]:
            result += 1
        else:
            result += 2
        return result


class Solution1:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        result = 1
        # 将数组前添加一个相等节点
        pre_diff = 0
        for i in range(0, len(nums)-1):
            cur_diff = nums[i+1] - nums[i]
            # 这里的=用来适配pre = 0的初始值
            if pre_diff >= 0 > cur_diff or pre_diff <= 0 < cur_diff:
                result += 1
                pre_diff = cur_diff
        return result


if __name__ == '__main__':
    s = Solution1()
    print(s.wiggleMaxLength([1,2,3,4,5,6,7,8,9]))
