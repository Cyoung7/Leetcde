#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 10_105.py
@time: 2025/4/27 下午6:16
@desc: 105.有向图的完全可达性
https://kamacoder.com/problempage.php?pid=1177
"""



def dfs_1(start, visited, graph):

    for i in graph[start]:
        if i not in visited:
            visited.add(i)
            dfs_1(i,visited, graph)


def main_1():
    """
    邻接表
    :return:
    """
    input_str = """4 4
1 2
2 1
1 3
2 4"""


    input_lines = input_str.split("\n")
    n, m = map(int, input_lines[0].split())
    # 邻接表
    graph = [[] for _ in range(n + 1)]

    for i in range(m):
        f, t = map(int, input_lines[i + 1].split())
        graph[f].append(t)

    # 记录所有遍历过的点
    visited = set()
    visited.add(1)
    dfs_1(1, visited, graph)

    print(1 if len(visited) == n else -1)


if __name__ == '__main__':
    main_1()
