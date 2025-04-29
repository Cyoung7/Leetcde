#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: chao yang
Contact: cryoung777@gmail.com
Time: 2025/4/29 11:11
File:19_floyd.py
Description: floyd算法：求所有点到所有点的最短距离
"""
import copy
import math


def floyd(graph, n):
    grid = copy.deepcopy(graph)

    # k一定是在最外层，这个遍历顺序才正确
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                # 动态规划的状态转移方程
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    # print(grid)
    return grid

def main():
    """
    floyd
    :return:
    """
    input_str = """7 3
1 2 4
2 5 6
3 6 8
2
1 2
2 3"""

    input_lines = input_str.split("\n")
    n, e = map(int, input_lines[0].split())


    graph = [[float('inf')] * (n+1) for _ in range(n+1)]
    for i in range(e):
        f, t, w = map(int, input_lines[i + 1].split())
        graph[f][t] = w
        graph[t][f] = w

    grid = floyd(graph, n)
    z = int(input_lines[e+1].strip())


    for i in range(z):
        f, t = map(int, input_lines[e+2+i].split())
        print(f, t, grid[f][t])


if __name__ == '__main__':
    main()
