#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 8_15 3Sum.py
@time: 2025/4/9 下午1:45
@desc:
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        核心思想：双指针法，需要对数组进行先排序
            如果不能排序的，就不能用双指针法，需要用hash
        :param nums:
        :return:
        """
        nums.sort()
        result: List[List[int]] = list()

        for i in range(len(nums)-2):
            # 对i进行去重
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # 对left和right进行去重
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 0]
    print(s.threeSum(nums))