#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 9_110.py
@time: 2025/4/27 下午5:25
@desc:110. 字符串接龙
https://kamacoder.com/problempage.php?pid=1183
"""
import collections


def have_edge(a: str, b: str):
    for i in range(len(a)):
        if a[i] != b[i]:
            if "{}{}{}".format(a[:i], b[i], a[i + 1:]) == b:
                return True
    return False


def bfs(start, end, graph):
    count = 1
    visited = set()
    queue = collections.deque()
    queue.append(start)
    visited.add(start)

    while queue:
        count += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            for next_node in graph[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    if next_node == end:
                        return count
                    queue.append(next_node)
    return 0


def main_1():
    """
    邻接表存储字符串之间的变换情况
    :return:
    """
    input_str = """6
abc def
efc
dbc
ebc
dec
dfc
yhn"""

    input_lines = input_str.split("\n")
    n = int(input_lines[0].strip())
    start_str, end_str = input_lines[1].split()
    # 邻接表
    graph = collections.defaultdict(list)
    str_list = list()
    str_list.append(start_str)
    str_list.append(end_str)
    for i in range(n):
        str_list.append(input_lines[i + 2].strip())

    # 创建一个双线联通的无向图
    for i in range(len(str_list) - 1):
        for j in range(i + 1, len(str_list)):
            if have_edge(str_list[i], str_list[j]):
                graph[str_list[i]].append(str_list[j])
                graph[str_list[j]].append(str_list[i])

    # 两个节点之间的距离
    result = bfs("abc", "yhn", graph)
    print(result)


if __name__ == '__main__':
    # print(have_edge("dbc", "dfc"))
    main_1()
