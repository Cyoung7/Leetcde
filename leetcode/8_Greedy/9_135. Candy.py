#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 9_135. Candy.py
@time: 2025/4/22 下午4:03
@desc:
"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        核心思想：两个维度的贪心，一个一个维度处理
        :param ratings:
        :return:
        """
        len_rating = len(ratings)
        candy_list = [1 for _ in range(len_rating)]

        # 分别从左往右，在从右往左，分别满足条件即可
        for i in range(1, len_rating):
            if ratings[i] > ratings[i - 1]:
                candy_list[i] = candy_list[i - 1] + 1

        for i in range(len_rating - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy_list[i] = max(candy_list[i + 1] + 1, candy_list[i])

        return sum(candy_list)


if __name__ == '__main__':
    s = Solution()
    print(s.candy([1,0,2]))