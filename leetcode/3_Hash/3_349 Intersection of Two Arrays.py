#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 3_349 Intersection of Two Arrays.py
@time: 2025/4/9 上午10:00
@desc:
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        主要要学会使用一种哈希数据结构
        :param nums1:
        :param nums2:
        :return:
        """
        hash_result = dict()
        for i in nums1:
            hash_result[i] = 1
        for i in nums2:
            if hash_result.get(i):
                hash_result[i] += 1
        result = []
        for key, value in hash_result.items():
            if value > 1:
                result.append(key)
        return result


if __name__ == '__main__':
    s = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(s.intersection(nums1, nums2))