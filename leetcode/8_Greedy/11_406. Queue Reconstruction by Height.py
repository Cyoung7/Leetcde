#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 11_406. Queue Reconstruction by Height.py
@time: 2025/4/22 下午4:43
@desc:
"""
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        非常难
        :param people:
        :return:
        """
        people.sort(key=lambda x: (-x[0], x[1]))
        result = list()
        for p in people:
            idx = p[1]
            if idx >= len(result):
                result.append(p)
            else:
                result.insert(idx, p)
        return result


if __name__ == '__main__':
    s = Solution()
    people = [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]
    print(s.reconstructQueue(people))