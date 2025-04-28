#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 4_101.Island Total Area.py
@time: 2025/4/27 下午3:01
@desc: 101. 孤岛的总面积
https://kamacoder.com/problempage.php?pid=1173
"""
import collections


def bfs(x, y, n, m, graph, visited):
    count = 0
    dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    queue = collections.deque()

    # 标记是否遍历，可以入队列前标记，可以出队列后标记，只要前后一致都可以
    # 入队前标记
    visited[x][y] = True
    count += 1
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
                count += 1
                queue.append([new_x, new_y])
    return count


def main_1():
    """
    邻接矩阵 + bfs来求岛屿总面积
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
                count = bfs(i, j, n, m, graph, visited)
                # 求岛屿总面积
                result += count
    print(result)


if __name__ == '__main__':
    main_1()
