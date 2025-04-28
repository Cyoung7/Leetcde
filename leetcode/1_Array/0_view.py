#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 0_view.py
@time: 2025/4/17 下午5:19
@desc:
"""
import math
from typing import List


class Solution:
    """
    一个交易价格数组，找出获利的最大利润
    例如：
    [2,8,1,3,5,4],先买后卖找出最大利润
    """

    def search(self, nums: List[int]) -> int:
        """
        还是双指针法，只是这个慢指针的移动方式还是比较考脑壳
        :param nums:
        :return:
        """
        low_point = nums[0]
        max_diff = -math.inf

        for i in range(1, len(nums)):
            fast_point = nums[i]
            # 一旦后面出现了最低值，前面低点的值就失去了锚点意义
            if fast_point < low_point:
                low_point = fast_point
                continue
            if fast_point - low_point > max_diff:
                max_diff = fast_point - low_point
        return max_diff


if __name__ == '__main__':
    s = Solution()
    print(s.search([2, 8, 1, 3, 5, 4]))
