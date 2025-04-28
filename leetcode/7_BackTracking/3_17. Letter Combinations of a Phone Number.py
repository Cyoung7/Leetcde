#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 3_17. Letter Combinations of a Phone Number.py
@time: 2025/4/18 上午9:12
@desc:
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char_dict = {
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        results = list()

        def dfs(sub_digits: str, tmp_path):
            nonlocal char_dict

            # 处理数字1的情况
            while len(sub_digits) > 0 and sub_digits[0] == "1":
                sub_digits = sub_digits[1:]

            if len(sub_digits) == 0:
                if tmp_path != "":
                    results.append(tmp_path)
                return

            first_digits = sub_digits[0]
            for c in char_dict[first_digits]:
                dfs(sub_digits[1:], "{}{}".format(tmp_path, c))
            return
        dfs(digits, "")
        return results


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))