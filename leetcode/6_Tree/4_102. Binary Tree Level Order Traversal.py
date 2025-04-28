#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 4_102. Binary Tree Level Order Traversal.py
@time: 2025/4/14 下午4:36
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        层次遍历就是广度优先搜索，BFS
        :param root:
        :return:
        """
        q = deque()
        value = list()
        if root:
            q.append(root)
        while q:
            level = []
            for _ in range(len(q)):
                tmp_node = q.popleft()
                level.append(tmp_node.val)
                if tmp_node.left:
                    q.append(tmp_node.left)
                if tmp_node.right:
                    q.append(tmp_node.right)
            value.append(level)
        return value
