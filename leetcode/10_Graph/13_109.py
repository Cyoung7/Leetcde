#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: chao yang
Contact: cryoung777@gmail.com
Time: 2025/4/28 13:16
File:13_109.py
Description: 109. 冗余连接II
https://kamacoder.com/problempage.php?pid=1182
"""
from collections import defaultdict


class UnionFind(object):
    """
    并查集
    """
    def __init__(self, n):
        self.father = [i for i in range(n+1)]


    def find(self, u):
        # 寻找根节点
        if u == self.father[u]:
            return u
        else:
            self.father[u] = self.find(self.father[u])
            return self.father[u]


    def is_same(self, u, v):
        # 是否是同一个集合
        return self.find(u) == self.find(v)

    def join(self, u,v):
        # 合并两个集合
        root_u = self.find(u)
        root_v = self.find(v)
        # 注意这里是连接两个根节点
        if root_u == root_v:
            return
        self.father[v] = root_u


def is_tree_after_remove_edge(edges, edge, n):
    # 初始化并查集
    u = UnionFind(n)

    for i in range(len(edges)):
        if i == edge:
            continue
        s, t = edges[i]
        if u.is_same(s, t):  # 成環，即不是有向樹
            return False
        else:  # 將s,t放入集合中
            u.join(s, t)
    return True


def get_remove_edge(edges, n):
    # 初始化并查集
    u = UnionFind(n)

    for s, t in edges:
        if u.is_same(s, t):
            print(s, t)
            return
        else:
            u.join(s, t)



def main_1():
    """
    并查集
    :return:
    """
    input_str = """3
1 2
1 3
2 3"""

    input_lines = input_str.split("\n")
    n = int(input_lines[0].strip())
    edges = list()
    in_degree = defaultdict(int)

    # 并查集实现
    u = UnionFind(n)

    for i in range(n):
        f, t = map(int, input_lines[i + 1].split())
        in_degree[t] += 1
        edges.append([f, t])

    vec = list()
    for i in range(n-1, -1, -1):
        if in_degree[edges[i][1]] == 2:
            vec.append(i)

    # 輸出
    if len(vec) > 0:
        # 情況一：刪除輸出順序靠後的邊
        if is_tree_after_remove_edge(edges, vec[0], n):
            print(edges[vec[0]][0], edges[vec[0]][1])
        # 情況二：只能刪除特定的邊
        else:
            print(edges[vec[1]][0], edges[vec[1]][1])
    else:
        # 情況三： 原圖有環
        get_remove_edge(edges,n)


if __name__ == '__main__':
    main_1()
