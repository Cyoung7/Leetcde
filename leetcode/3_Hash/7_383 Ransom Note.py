#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 7_383 Ransom Note.py
@time: 2025/4/9 下午1:17
@desc:
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        核心思想：利用hash结构存储字符出现的次数
        :param ransomNote:
        :param magazine:
        :return:
        """
        char_dict = dict()
        for m in magazine:
            if char_dict.get(m) is None:
                char_dict[m] = 1
            else:
                char_dict[m] += 1

        for r in ransomNote:
            if char_dict.get(r) is None:
                return False
            char_dict[r] -= 1
            if char_dict[r] < 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()