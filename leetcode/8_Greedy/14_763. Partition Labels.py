#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 14_763. Partition Labels.py
@time: 2025/4/22 下午8:28
@desc:
"""
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        char_last_idx = dict()
        # 先统计每个字符最后出现的位置
        for idx, c in enumerate(s):
            char_last_idx[c] = idx

        results = list()

        pre_bound = -1
        cur_bound = 0
        for idx, c in enumerate(s):
            # 走到最后一个字符出现的位置，而且这个字符是之前字符的最远边界
            if idx == char_last_idx[c] == cur_bound:
                results.append(cur_bound - pre_bound)
                pre_bound = cur_bound
                cur_bound += 1
            else:
                # 贪心，找最远边界
                cur_bound = max(cur_bound, char_last_idx[c])
        return results


if __name__ == '__main__':
    s = Solution()
    print(s.partitionLabels("vhaagbqkaq"))