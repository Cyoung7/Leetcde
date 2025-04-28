#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 3_151. Reverse Words in a String.py
@time: 2025/4/10 上午10:39
@desc:
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        不用split，reverse方法，用了这题就水题了
        :param s:
        :return:
        """
        # 开头加一个空格，方便统一处理，类似于链表加一个虚拟头
        s = " " + s

        idx_start = len(s)-1
        idx_end = idx_start + 1  # 左闭右开区间
        s_list = []

        while idx_start > 0:
            # 是空格前后指针都往前移动
            while s[idx_start] == " ":
                idx_start -= 1
                idx_end -= 1
                if idx_start == 0:
                    break
            # 非空格前指针都往前移动
            while idx_start > 0 and s[idx_start] != " ":
                idx_start -= 1

            # 只有真正字符串才加
            if idx_start+1 != idx_end:
                s_list.append(s[idx_start+1: idx_end])
            idx_end = idx_start+1

        return " ".join(s_list)


class Solution1:
    """
    提升难度，不使用额外空间，空间复杂度O(1)
        1.先去除多余空格
        2.反转整个字符串
        3.反转每个单词
    """
    def reverseWords(self, s: str) -> str:
        pass


if __name__ == '__main__':
    s = Solution()
    s_str = "       the sky"
    print(s.reverseWords(s_str))