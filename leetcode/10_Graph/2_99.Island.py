#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 2_99.Island.py
@time: 2025/4/27 下午1:58
@desc: 99. 岛屿数量
https://kamacoder.com/problempage.php?pid=1171
"""
import collections


def dfs(x, y, n, m, graph, visited):
    dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    for d in dirs:
        new_x = x + d[0]
        new_y = y + d[1]
        if new_x < 0 or new_x == n or new_y < 0 or new_y == m:
            continue
        if graph[new_x][new_y] == 1 and visited[new_x][new_y] is False:
            visited[new_x][new_y] = True
            dfs(new_x, new_y, n, m, graph, visited)


def main():
    """
    邻接矩阵 + dfs来判断岛屿的数量
    :return:
    """
    input_str = """4 5
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1"""

    input_lines = input_str.split("\n")
    n, m = map(int, input_lines[0].split())
    # 邻接矩阵
    graph = []
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        graph.append(list(map(int, input_lines[i + 1].split())))

    result = 0
    for i in range(n):
        for j in range(m):
            # 找到一个没有被搜索过的陆地，把这块陆地相邻的陆地都搜索一遍
            if visited[i][j] is False and graph[i][j] == 1:
                result += 1
                visited[i][j] = True
                dfs(i, j, n, m, graph, visited)
    print(result)


def bfs(x, y, n, m, graph, visited):
    dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    queue = collections.deque()

    # 标记是否遍历，可以入队列前标记，可以出队列后标记，只要前后一致都可以
    # 入队前标记
    visited[x][y] = True
    queue.append([x, y])

    while queue:
        tmp_x, tmp_y = queue.popleft()
        for d in dirs:
            new_x = tmp_x + d[0]
            new_y = tmp_y + d[1]
            if new_x < 0 or new_x == n or new_y < 0 or new_y == m:
                continue
            if graph[new_x][new_y] == 1 and visited[new_x][new_y] is False:
                # 入队前标记
                visited[new_x][new_y] = True
                queue.append([new_x, new_y])


def main_1():
    """
    邻接矩阵 + bfs来判断岛屿的数量
    :return:
    """
    input_str = """4 5
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1"""

    input_lines = input_str.split("\n")
    n, m = map(int, input_lines[0].split())
    # 邻接矩阵
    graph = []
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        graph.append(list(map(int, input_lines[i + 1].split())))

    result = 0
    for i in range(n):
        for j in range(m):
            # 找到一个没有被搜索过的陆地，把这块陆地相邻的陆地都搜索一遍
            if visited[i][j] is False and graph[i][j] == 1:
                result += 1
                bfs(i, j, n, m, graph, visited)
    print(result)


if __name__ == '__main__':
    # dfs
    # main()

    # bfs
    main_1()
