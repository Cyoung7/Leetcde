#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 8_106.py
@time: 2025/4/27 下午4:45
@desc: 106. 岛屿的周长
https://kamacoder.com/problempage.php?pid=1178
"""


def main_1():
    """
    邻接矩阵: 求岛屿的周长
    不需要dfs，或bfs搜索
    :return:
    """
    input_str = """5 5
0 0 0 0 0
0 1 0 1 0
0 1 1 1 0
0 1 1 1 0
0 0 0 0 0"""

    input_lines = input_str.split("\n")
    n, m = map(int, input_lines[0].split())
    # 邻接矩阵
    graph = []

    for i in range(n):
        graph.append(list(map(int, input_lines[i + 1].split())))

    sum_i = 0
    cover = 0
    for i in range(n):
        for j in range(m):
            # 找到一个没有被搜索过的陆地，把这块陆地相邻的陆地都搜索一遍
            if graph[i][j] == 1:
                sum_i += 1
                if i - 1 >= 0 and graph[i - 1][j] == 1:
                    cover += 1
                if j - 1 >= 0 and graph[i][j - 1] == 1:
                    cover += 1
    # 每个单独的陆地，4条边，如果两个陆地紧挨，减少两条边
    print(sum_i * 4 - 2 * cover)


if __name__ == '__main__':
    main_1()
