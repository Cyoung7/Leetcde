#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: chao yang
Contact: cryoung777@gmail.com
Time: 2025/4/28 15:42
File:17_dijkstra.py
Description:最短路径算法, dijkstra算法
"""
import heapq
from collections import defaultdict


def dijkstra(graph, n):
    """
    朴素的dijkstra算法，每一次找距离起始节点最近的节点进行操作
    :param graph:
    :param n:
    :return:
    """
    min_dist = [float('inf')] * (n+1)
    min_dist[1] = 0
    visited = [False] * (n+1)

    for _ in range(1, n+1):
        cur = -1
        tmp_min_dist = float('inf')
        # 找到里起点最近的节点
        for j in range(1, n+1):
            if visited[j] is False and min_dist[j] < tmp_min_dist:
                tmp_min_dist = min_dist[j]
                cur = j
        # 标记访问
        visited[cur] = True

        # 更新下一个节点的最近距离
        for j in range(1, n + 1):
            if visited[j] is False and graph[cur][j] + min_dist[cur] < min_dist[j]:
                min_dist[j] = graph[cur][j] + min_dist[cur]
    # 多有节点与起始节点的最短距离
    print(min_dist)
    return min_dist[-1]

def main_1():
    """
    dijkstra:利用邻接矩阵存储图，两层for遍历节点
    :return:
    """
    input_str = """7 9
1 2 1
1 3 4
2 3 2
2 4 5
3 4 2
4 5 3
2 6 4
5 7 4
6 7 9"""

    input_lines = input_str.split("\n")
    n, e = map(int, input_lines[0].split())


    graph = [[10001] * (n+1) for _ in range(n+1)]
    for i in range(e):
        f, t, w = map(int, input_lines[i + 1].split())
        graph[f][t] = w
        graph[t][f] = w
    print(dijkstra(graph, n))


def dijkstra_v2(graph, n):
    """
    dijkstra:优化方案,利用堆来自动找到距离起始节点最近的节点
    :param graph:
    :param n:
    :return:
    """
    min_dist = [float('inf')] * (n+1)
    min_dist[1] = 0
    visited = [False] * (n+1)

    pq = list()  # (distance, node)
    # 将起始节点加入
    heapq.heappush(pq, (0, 1))
    while pq:
        # 每次取距离起始节点最小的节点
        dis, cur = heapq.heappop(pq)
        if visited[cur]:
            continue
        visited[cur] = True

        for e in graph[cur]:
            # e[0]:node  e[1]:weight
            # 找起点到e[0]更近的距离
            if visited[e[0]] is False and dis + e[1] < min_dist[e[0]]:
                min_dist[e[0]] = dis + e[1]
                heapq.heappush(pq, (min_dist[e[0]], e[0]))
    print(min_dist)
    return min_dist[-1]


def main():
    """
    dijkstra: 利用邻接表存储图，小顶堆来处理最短距离节点
    :return:
    """
    input_str = """7 9
1 2 1
1 3 4
2 3 2
2 4 5
3 4 2
4 5 3
2 6 4
5 7 4
6 7 9"""

    input_lines = input_str.split("\n")
    n, e = map(int, input_lines[0].split())

    graph = defaultdict(list)
    for i in range(e):
        f, t, w = map(int, input_lines[i + 1].split())
        # 将节点和权重一起存
        graph[f].append((t, w))
        graph[t].append((f, w))

    print(dijkstra_v2(graph, n))


if __name__ == '__main__':
    # main()
    main_1()