#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 15_51. N-Queens.py
@time: 2025/4/18 下午3:59
@desc:
"""
import copy
from typing import List


class Solution:
    def is_valid(self, row, col, chessboard):
        for i in range(row):
            if chessboard[i][col] == "Q":
                return False
        # 检查 45 度角是否有皇后
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False  # 左上方向已经存在皇后，不合法
            i -= 1
            j -= 1

        # 检查 135 度角是否有皇后
        i, j = row - 1, col + 1
        while i >= 0 and j < len(chessboard):
            if chessboard[i][j] == 'Q':
                return False  # 右上方向已经存在皇后，不合法
            i -= 1
            j += 1

        return True  # 当前位置合法

    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        主要难度就是在这个判断条件上
        :param n:
        :return:
        """
        results = list()
        chessboard = ["." * n for _ in range(n)]

        def dfs(row):
            nonlocal n, chessboard, results
            if row == n:
                results.append(copy.copy(chessboard))
                return

            for col in range(n):
                # 主要难度就是在这个判断条件上
                if self.is_valid(row, col, chessboard):
                    chessboard[row] = chessboard[row][:col] + 'Q' + chessboard[row][col+1:]  # 放置皇后
                    dfs(row+1)
                    chessboard[row] = chessboard[row][:col] + '.' + chessboard[row][col+1:]
            return
        dfs(0)
        return results


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))