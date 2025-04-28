#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 9_416. Partition Equal Subset Sum.py
@time: 2025/4/23 下午1:51
@desc:
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        dp[i]:
        :param nums:
        :return:
        """
        sum_num = sum(nums)
        value = int(sum_num / 2)
        if value * 2 != sum_num:
            return False

        dp = [0] * (value+1)

        for num in nums:
            for i in range(value, num-1, -1):
                dp[i] = max(dp[i], dp[i-num] + num)

        if dp[value] == value:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    s.canPartition([3, 3, 3, 4, 5])
