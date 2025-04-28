#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 16_37. Sudoku Solver.py
@time: 2025/4/18 下午4:16
@desc:
"""
import copy
from typing import List


class Solution:
    def is_valid(self, row, col, k, board):
        for i in range(9):
            if board[row][i] == k:
                return False
        for j in range(9):
            if board[j][col] == k:
                return False

        start_row = int(row / 3) * 3
        start_col = int(col / 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == k:
                    return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        AC不过，超时
        Do not return anything, modify board in-place instead.
        """

        def dfs():
            nonlocal board
            for i in range(9):
                for j in range(9):
                    if board[i][j] != ".":
                        continue
                    for k in range(1, 10):
                        if self.is_valid(i, j, str(k), board):
                            board[i][j] = str(k)
                            if dfs():
                                return True
                            board[i][j] = "."
                    return False
            return True

        dfs()


if __name__ == '__main__':
    board = [[".", ".", ".", ".", ".", ".", ".", ".", "."], [".", "9", ".", ".", "1", ".", ".", "3", "."],
             [".", ".", "6", ".", "2", ".", "7", ".", "."], [".", ".", ".", "3", ".", "4", ".", ".", "."],
             ["2", "1", ".", ".", ".", ".", ".", "9", "8"], [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", "2", "5", ".", "6", "4", ".", "."], [".", "8", ".", ".", ".", ".", ".", "1", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."]]

    s = Solution()
    s.solveSudoku(board)
    print(board)
