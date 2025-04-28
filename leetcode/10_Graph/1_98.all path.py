#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 1_98.all path.py
@time: 2025/4/27 下午1:00
@desc:98. 所有可达路径
https://kamacoder.com/problempage.php?pid=1170
"""


def dfs(start, end, path, result, graph):
    if start == end:
        result.append(" ".join(map(str, path)))
        return
    for i in range(1, end + 1):
        if graph[start][i] == 1:
            path.append(i)
            dfs(i, end, path, result, graph)
            path.pop()


def main():
    """
    邻接矩阵
    :return:
    """
    input_str = """5 5
    1 3
    3 5
    1 2
    2 4
    4 5"""

    input_lines = input_str.split("\n")
    n, m = map(int, input_lines[0].split())
    # 邻接矩阵
    graph = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(m):
        f, t = map(int, input_lines[i + 1].split())
        graph[f][t] = 1

    result = list()
    path = list()

    path.append(1)
    dfs(1, n, path, result, graph)
    print(result)


def dfs_1(start, end, path, result, graph):
    if start == end:
        result.append(" ".join(map(str, path)))
        return

    for i in graph[start]:
        path.append(i)
        dfs_1(i, end, path, result, graph)
        path.pop()


def main_1():
    """
    邻接表
    :return:
    """
    input_str = """5 5
    1 3
    3 5
    1 2
    2 4
    4 5"""

    input_lines = input_str.split("\n")
    n, m = map(int, input_lines[0].split())
    # 邻接表
    graph = [[] for _ in range(n + 1)]

    for i in range(m):
        f, t = map(int, input_lines[i + 1].split())
        graph[f].append(t)

    result = list()
    path = list()
    path.append(1)
    dfs_1(1, n, path, result, graph)
    print(result)


if __name__ == '__main__':
    # main()
    main_1()
