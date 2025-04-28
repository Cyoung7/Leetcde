#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 6_103.Water Flow Problem.py
@time: 2025/4/27 下午3:35
@desc: 103. 水流问题
https://kamacoder.com/problempage.php?pid=1175
"""
import collections


def bfs(x, y, n, m, graph, visited):
    v_set = set()
    dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    queue = collections.deque()

    # 标记是否遍历，可以入队列前标记，可以出队列后标记，只要前后一致都可以
    # 入队前标记
    visited[x][y] = True
    v_set.add("{} {}".format(x, y))
    queue.append([x, y])

    while queue:
        tmp_x, tmp_y = queue.popleft()
        for d in dirs:
            new_x = tmp_x + d[0]
            new_y = tmp_y + d[1]
            if new_x < 0 or new_x == n or new_y < 0 or new_y == m:
                continue
            # 反向思想，往高处遍历
            if graph[new_x][new_y] >= graph[tmp_x][tmp_y] and visited[new_x][new_y] is False:
                # 入队前标记
                visited[new_x][new_y] = True
                v_set.add("{} {}".format(new_x, new_y))
                queue.append([new_x, new_y])
    return v_set


def main_1():
    """
    邻接矩阵 + bfs来求岛屿总面积
    :return:
    """
    input_str = """5 5
1 3 1 2 4
1 2 1 3 2
2 4 7 2 1
4 5 6 1 1
1 4 1 2 1"""

    input_lines = input_str.split("\n")
    n, m = map(int, input_lines[0].split())
    # 邻接矩阵
    graph = []

    for i in range(n):
        graph.append(list(map(int, input_lines[i + 1].split())))

    result1 = set()
    visited_1 = [[False] * m for _ in range(n)]
    # 第一组边界遍历
    # 从边界往高处遍历
    for i in range(n):
        if visited_1[i][0] is False:
            result1 = result1.union(bfs(i, 0, n, m, graph, visited_1))

    for j in range(m):
        if visited_1[0][j] is False:
            result1 = result1.union(bfs(0, j, n, m, graph, visited_1))

    # 第二组边界遍历
    # 从边界往高处遍历
    result2 = set()
    visited_2 = [[False] * m for _ in range(n)]
    for i in range(n):
        if visited_2[i][m-1] is False:
            result2 = result2.union(bfs(i, m-1, n, m, graph, visited_2))
    for j in range(m):
        if visited_2[n-1][j] is False:
            result2 = result2.union(bfs(n-1, j, n, m, graph, visited_2))

    # 两组的交集就是都能往两边低出边界流的坐标
    # print
    print("\n".join(result1.intersection(result2)))


if __name__ == '__main__':
    main_1()
