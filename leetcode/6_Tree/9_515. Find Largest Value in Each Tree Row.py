#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 9_515. Find Largest Value in Each Tree Row.py
@time: 2025/4/14 下午5:56
@desc:
"""
import math
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
        BFS层次遍历，记录每一层最大值,和7_637求平均值异曲同工
        :param root:
        :return:
        """
        value = list()
        queue = deque()
        if root:
            queue.append(root)

        while queue:
            level_max = -math.inf
            level_len = len(queue)
            for i in range(level_len):
                tmp_node = queue.popleft()
                if tmp_node.left:
                    queue.append(tmp_node.left)
                if tmp_node.right:
                    queue.append(tmp_node.right)
                level_max = max(level_max, tmp_node.val)
            value.append(level_max)
        return value
