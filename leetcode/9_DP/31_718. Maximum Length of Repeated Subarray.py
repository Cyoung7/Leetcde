#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 31_718. Maximum Length of Repeated Subarray.py
@time: 2025/4/25 上午9:57
@desc:
"""
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        # # dp[i][j]表示nums2 [以nums2[i]结尾] 与 nums1 [以nums1[j]结尾]的最长子序列长度
        dp = [[0]*len(nums1) for _ in range(len(nums2))]

        for i in range(0, len(nums2)):
            for j in range(0, len(nums1)):
                # 状态转移方程
                if nums2[i] == nums1[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # 状态转移方程
                        dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > result:
                    result = dp[i][j]
        return result

class Solution1:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        和上面的差别就是不用处理j==0，i==0的特殊情况
        :param nums1:
        :param nums2:
        :return:
        """
        result = 0
        # dp[i][j]表示nums1 [以nums[i-1]结尾] 与 nums2 [以nums2[j-1]结尾]的最长子序列长度
        dp = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]

        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    # 状态转移方程
                    dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > result:
                    result = dp[i][j]
        return result


if __name__ == '__main__':
    s = Solution()
    s.findLength([0,0,0,0,1], [1,0,0,0,0])