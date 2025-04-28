#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 1_797. All Paths From Source to Target.py
@time: 2025/4/27 下午1:33
@desc: leetcode 797
"""
import copy
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        根据graph的参数，这个graph是以邻接表的形式存储图结构的
        题目限定有向无环，所以不需要判断节点是否遍历过的问题，一个节点不会被重复遍历
        :param graph:
        :return:
        """
        path = list()
        results = list()

        def dfs(start, end):
            nonlocal path, results, graph
            if start == end:
                results.append(copy.copy(path))

            for i in graph[start]:
                path.append(i)
                dfs(i, end)
                path.pop()
            return

        path.append(0)
        dfs(0, len(graph)-1)
        return results
