#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 10_860. Lemonade Change.py
@time: 2025/4/22 下午4:21
@desc:
"""
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        直接模拟
        :param bills:
        :return:
        """
        five_num = 0
        ten_num = 0
        tw_num = 0

        for b in bills:
            if b == 5:
                five_num += 1
            elif b == 10:
                ten_num += 1
                if five_num > 0:
                    five_num -= 1
                else:
                    return False
            else:
                tw_num += 1
                # 这里给20找零，有点贪心，先用10块的
                if ten_num > 0:
                    ten_num -= 1
                    if five_num > 0:
                        five_num -= 1
                    else:
                        return False
                else:
                    if five_num >= 3:
                        five_num -= 3
                    else:
                        return False
        return True
