#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: chao yang
Contact: cryoung777@gmail.com
Time: 2025/4/28 15:02
File:16_topologic_sort.py
Description: 拓扑排序
"""
from collections import defaultdict, deque


def topologic_sort(edges, n):
    """
    bfs
    核心思想：
        1.遍历入度为0的节点（dfs层次遍历）
        2.遍历过的节点删除
    :param edges:
    :param n:
    :return:
    """
    in_degree = [0] * n
    # 使用邻接表存储graph
    graph = defaultdict(list)
    for e in edges:
        in_degree[e[1]] += 1
        graph[e[0]].append(e[1])

    queue = deque([i for i in range(n) if in_degree[i] == 0])

    result = []
    while queue:
        f = queue.popleft()
        result.append(f)
        for t in graph[f]:
            # 将遍历过的节点删除
            in_degree[t] -= 1
            if in_degree[t] == 0:
                queue.append(t)

    # 如果不是所有边都加进来，说明一定出现了环
    if len(result) == n:
        return " ".join(result)
    else:
        return "-1"

def main_1():
    """
    :return:
    """
    input_str = """5 4
0 1
0 2
1 3
2 4"""

    input_lines = input_str.split("\n")
    n, e = map(int, input_lines[0].split())
    edges = list()

    for i in range(e):
        f, t= map(int, input_lines[i + 1].split())
        edges.append([f, t])

    print(topologic_sort(edges, n))



if __name__ == '__main__':
    main_1()
