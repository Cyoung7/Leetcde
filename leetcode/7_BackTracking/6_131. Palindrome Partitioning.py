#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 6_131. Palindrome Partitioning.py
@time: 2025/4/18 上午10:21
@desc:
"""
import copy
from typing import List


class Solution:
    def is_palindrome(self, s: str) -> bool:
        """
        判断字符串是否是回文字符串（忽略大小写和非字母数字字符）。
        待优化：利用动态规划判断回文字符串
        """
        # # 将字符串转换为小写，并过滤非字母数字字符
        # cleaned = ''.join(char.lower() for char in s if char.isalnum())
        #
        # # 方法 1：比较正序和倒序
        return s == s[::-1]

        # 方法 2：双指针（可选，性能更高）
        # left, right = 0, len(s) - 1
        # while left < right:
        #     if s[left] != s[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True

    def partition(self, s: str) -> List[List[str]]:
        results = list()
        tmp_result = list()

        def dfs(tmp_s: str):
            if len(tmp_s) == 0:
                results.append(copy.copy(tmp_result))
                return

            for end in range(1, len(tmp_s)+1):
                # end这里是开区间，上面range的结束应该len+1
                tmp_str = tmp_s[:end]
                if self.is_palindrome(tmp_str):
                    tmp_result.append(tmp_str)
                    dfs(tmp_s[end:])
                    tmp_result.pop()
            return

        dfs(s)
        return results


if __name__ == '__main__':
    s = Solution()
    print(s.partition("aab"))
