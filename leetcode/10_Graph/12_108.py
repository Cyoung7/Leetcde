#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: chao yang
Contact: cryoung777@gmail.com
Time: 2025/4/28 12:56
File:12_108.py
Description: 0108.冗余连接
https://kamacoder.com/problempage.php?pid=1181
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
    input_str = """3
1 2
2 3
1 3"""


    input_lines = input_str.split("\n")
    n = int(input_lines[0].strip())

    # 并查集实现
    u = UnionFind(n)

    for i in range(n):
        f, t = map(int, input_lines[i + 1].split())
        # 如果两个节点都出现在同一个集合里，如果再加一条边，一定就形成了环
        if u.is_same(f, t):
            print(input_lines[i+1].strip())
            return
        u.join(f, t)



if __name__ == '__main__':
    main_1()
