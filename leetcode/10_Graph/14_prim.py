#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: chao yang
Contact: cryoung777@gmail.com
Time: 2025/4/28 14:00
File:14_prim.py
Description: 最小生成树 prim算法
"""




def prim(graph, n):
    visited = [False] * (n+1)
    min_dist = [10001] * (n+1)

    min_dist[1] = 0

    # n个节点，重复n次动作
    for _ in range(1, n+1):
        min_val = 10002
        cur = -1
        # 选当前距离最小生成树最近距离的节点
        for j in range(1, n+1):
            if visited[j] is False and min_dist[j] < min_val:
                min_val = min_dist[j]
                cur = j
        # 添加该节点
        visited[cur] = True

        # 将与该节点联通的节点，更新节点与最小生成树的连接值
        for j in range(1, n+1):
            if visited[j] is False and graph[cur][j] < min_dist[j]:
                min_dist[j] = graph[cur][j]

    result = 0
    for i in range(2, n+1):
        result += min_dist[i]
    return result


def main_1():
    """
    prim
    :return:
    """
    input_str = """7 11
1 2 1
1 3 1
1 5 2
2 6 1
2 4 2
2 3 2
3 4 1
4 5 1
5 6 2
5 7 1
6 7 1"""

    input_lines = input_str.split("\n")
    n, e = map(int, input_lines[0].split())
    graph = [[10001] * (n+1) for _ in range(n+1)]

    for i in range(e):
        f, t, w = map(int, input_lines[i + 1].split())
        graph[f][t] = w
        graph[t][f] = w
    print(prim(graph, n))

if __name__ == '__main__':
    main_1()
