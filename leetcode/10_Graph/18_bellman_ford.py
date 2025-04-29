#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: chao yang
Contact: cryoung777@gmail.com
Time: 2025/4/29 09:42
File:18_bellman_ford.py
Description: 最短路径算法, bellman_ford 算法
"""
import collections
from sys import flags


def bellman_ford(edges, n):
    """
    边中不存在负权回路，所以n-1次松弛和n次，2n次松弛，结果都是一样的
    :param edges:
    :param n:
    :return:
    """
    min_dist = [float('inf')] * (n+1)
    start = 1
    end = n
    min_dist[start] = 0

    # 进行n-1次松弛, 1到n之间最多n-1条边
    for i in range(n-1):
        for edge in edges:
            f, t, w = edge
            if min_dist[f] != float('inf'):
                min_dist[t] = min(min_dist[t], min_dist[f] + w)
        print(min_dist)
    return min_dist[n]

def main():
    """
    bellman_ford: 直接利用边,来计算每个节点到起始节点的最短距离
    :return:
    """
    input_str = """6 7
5 6 -2
1 2 1
5 3 1
2 5 2
2 4 -3
4 6 4
1 3 5"""

    input_lines = input_str.split("\n")
    n, e = map(int, input_lines[0].split())

    edges = list()
    for i in range(e):
        f, t, w = map(int, input_lines[i + 1].split())
        edges.append((f, t, w))

    print(bellman_ford(edges, n))

def bellman_ford_v2(graph, n):
    """
    优化版，避免每次都对所有边进行松弛
    只有之前松弛过的节点，才有必要堆节点的下一条边进行松弛
    而且不一定要松弛n-1次，所有松弛结束，即可结束
    :param graph:
    :param n:
    :return:
    """
    min_dist = [float('inf')] * (n+1)
    start = 1
    end = n
    min_dist[start] = 0

    #避免节点重复加入队列
    in_queue = [False] * (n + 1)
    queue = collections.deque([start])
    in_queue[start] = True

    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            in_queue[current] = False
            for e in graph[current]:
                if min_dist[e[0]] > min_dist[current] + e[1]:
                    min_dist[e[0]] = min_dist[current] + e[1]
                    if in_queue[e[0]] is False:
                        queue.append(e[0])
                        in_queue[e[0]] = True
        print(min_dist)
    return min_dist[end]


def main_1():
    """
    bellman_ford 优化版，利用邻接表来存储图
    :return:
    """
    input_str = """6 7
5 6 -2
1 2 1
5 3 1
2 5 2
2 4 -3
4 6 4
1 3 5"""

    input_lines = input_str.split("\n")
    n, e = map(int, input_lines[0].split())

    graph = collections.defaultdict(list)
    for i in range(e):
        f, t, w = map(int, input_lines[i + 1].split())
        # 将节点和权重一起存,单向图
        graph[f].append((t, w))
        # graph[t].append((f, w))

    print(bellman_ford_v2(graph, n))


# 以下是对负权回路的处理
def bellman_ford_v3(edges, n):
    """
    边中不存在负权回路，所以n-1次松弛和n次，2n次松弛，结果都是一样的
    :param edges:
    :param n:
    :return:
    """
    min_dist = [float('inf')] * (n+1)
    start = 1
    end = n
    min_dist[start] = 0

    flag = False
    # 进行n次松弛, 利用最后一次松弛判断是否存在负权回路
    for i in range(1, n+1):
        for edge in edges:
            f, t, w = edge
            if i < n:
                if min_dist[f] != float('inf'):
                    min_dist[t] = min(min_dist[t], min_dist[f] + w)
            else:
                if min_dist[f] != float('inf'):
                    min_dist[t] = min(min_dist[t], min_dist[f] + w)
                    flag = True

        print(min_dist)
    if flag:
        print("circle")
    return min_dist[end]


def main_3():
    """
    :return:
    """
    input_str = """4 4
1 2 -1
2 3 1
3 1 -1
3 4 1"""

    input_lines = input_str.split("\n")
    n, e = map(int, input_lines[0].split())

    edges = list()
    for i in range(e):
        f, t, w = map(int, input_lines[i + 1].split())
        edges.append((f, t, w))

    print(bellman_ford_v3(edges, n))

def bellman_ford_v4(graph, n):
    """
    优化版，避免每次都对所有边进行松弛
    只有之前松弛过的节点，才有必要堆节点的下一条边进行松弛
    而且不一定要松弛n-1次，所有松弛结束，即可结束
    :param graph:
    :param n:
    :return:
    """
    min_dist = [float('inf')] * (n+1)
    start = 1
    end = n
    min_dist[start] = 0

    #避免节点重复加入队列
    in_queue = [False] * (n + 1)
    queue = collections.deque([start])
    in_queue[start] = True

    # 如果入队列次数超过了n次，一定存在负权回路
    circle = 0
    while queue:
        circle += 1
        if circle > n:
            break
        for _ in range(len(queue)):
            current = queue.popleft()
            in_queue[current] = False
            for e in graph[current]:
                if min_dist[e[0]] > min_dist[current] + e[1]:
                    min_dist[e[0]] = min_dist[current] + e[1]
                    if in_queue[e[0]] is False:
                        queue.append(e[0])
                        in_queue[e[0]] = True
        print(min_dist)
    if circle > n:
        print("circle")
    return min_dist[end]


def main_4():
    """

    :return:
    """
    input_str = """4 4
1 2 -1
2 3 1
3 1 -1
3 4 1"""

    input_lines = input_str.split("\n")
    n, e = map(int, input_lines[0].split())

    graph = collections.defaultdict(list)
    for i in range(e):
        f, t, w = map(int, input_lines[i + 1].split())
        # 将节点和权重一起存,单向图
        graph[f].append((t, w))
        # graph[t].append((f, w))

    print(bellman_ford_v4(graph, n))



if __name__ == '__main__':
    # main()
    # print("\n")
    # main_1()

    # 负权回路检测
    main_3()
    print("\n")
    main_4()