#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 7_93. Restore IP Addresses.py
@time: 2025/4/18 上午10:50
@desc:
"""
from typing import List


class Solution:
    def is_valid_num(self, tmp_s: str):
        int_s = int(tmp_s)
        if int_s > 0 and tmp_s[0] == "0":
            return False
        if int_s > 255:
            return False
        if int_s == 0 and len(tmp_s) > 1:
            return False
        return True

    def restoreIpAddresses(self, s: str) -> List[str]:
        results = list()
        path_value = list()

        def dfs(tmp_s: str, k):
            if len(tmp_s) == 0 and k == 4:
                results.append(".".join(path_value))
                return
            # if k >= 4:
            #     return
            for end in range(1, len(tmp_s)+1):
                tmp_str = tmp_s[: end]
                # 这里控制k，上面就不用判断了
                if k < 4 and end < 4 and self.is_valid_num(tmp_str):
                    path_value.append(tmp_str)
                    dfs(tmp_s[end:], k+1)
                    path_value.pop()
            return
        dfs(s, 0)
        return results


if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses("0000"))
