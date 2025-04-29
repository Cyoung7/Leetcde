#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: chao yang
Contact: cryoung777@gmail.com
Time: 2025/4/28 14:22
File:15_kruskal.py
Description: 最小生成树 kruskal算法
"""


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

def kruskal(edges, n):
    # 优先添加小边
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)

    ans = 0
    for e in edges:
        u, v, w = e[0], e[1], e[2]
        if not uf.is_same(u, v):
            ans += w
            uf.join(u, v)
    return ans


def main_1():
    """
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
    edges = list()

    for i in range(e):
        f, t, w = map(int, input_lines[i + 1].split())
        edges.append([f, t, w])

    print(kruskal(edges, n))



if __name__ == '__main__':
    main_1()
