#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: chao yang
Contact: cryoung777@gmail.com
Time: 2025/4/28 11:53
File:11_107.py
Description:  0107.寻找存在的路径
https://kamacoder.com/problempage.php?pid=1179
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


def main_1():
    """
    并查集
    :return:
    """
    input_str = """5 4
1 2
1 3
2 4
3 4
1 4"""


    input_lines = input_str.split("\n")
    n, m = map(int, input_lines[0].split())

    # 并查集实现
    u = UnionFind(n)

    for i in range(m):
        f, t = map(int, input_lines[i + 1].split())
        u.join(f, t)

    start, end = map(int, input_lines[-1].split())

    print(u.is_same(start, end))


if __name__ == '__main__':
    main_1()
