#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 2_1002 Find Common Characters.py
@time: 2025/4/9 上午9:26
@desc:
"""
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """
        核心思想：
        hash表记录每个字符串的字符出现次数
        分别为每一个字符串单独记录hash表
        取每个hash表中对应位置最小的值就是字符在所有字符串中共同出现的次数
        :param words:
        :return:
        """
        arr_count = [0 for i in range(26)]
        for i in range(len(words[0])):
            arr_count[ord(words[0][i]) - 97] += 1

        for i in range(1, len(words)):
            other_count = [0 for i in range(26)]
            for j in range(len(words[i])):
                other_count[ord(words[i][j]) - 97] += 1

            for k in range(len(arr_count)):
                arr_count[k] = min(arr_count[k], other_count[k])

        char_list = []
        for idx, count in enumerate(arr_count):
            if count > 0:
                for i in range(count):
                    char_list.append(chr(idx+97))
        return char_list


if __name__ == '__main__':
    s = Solution()
    print(s.commonChars(["bella","label","roller"]))
