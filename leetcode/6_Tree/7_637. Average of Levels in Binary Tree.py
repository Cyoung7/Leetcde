#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 7_637. Average of Levels in Binary Tree.py
@time: 2025/4/14 下午5:25
@desc:
"""
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        BFS层次遍历，记录每一层平均值
        :param root:
        :return:
        """
        value = list()
        queue = deque()
        if root:
            queue.append(root)

        while queue:
            level_sum = 0
            level_len = len(queue)
            for i in range(level_len):
                tmp_node = queue.popleft()
                if tmp_node.left:
                    queue.append(tmp_node.left)
                if tmp_node.right:
                    queue.append(tmp_node.right)
                level_sum += tmp_node.val
            value.append(level_sum / level_len)
        return value
