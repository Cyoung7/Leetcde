#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 12_111. Minimum Depth of Binary Tree.py
@time: 2025/4/14 下午6:42
@desc:
"""
import collections
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        BFS层次遍历,只要遇到无子节点的节点，直接结束
        :param root:
        :return:
        """
        queue = collections.deque()
        if root:
            queue.append(root)
        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):
                tmp_node = queue.popleft()
                # 只要遇到无子节点的节点，直接结束
                if tmp_node.left is None and tmp_node.right is None:
                    return depth
                if tmp_node.left:
                    queue.append(tmp_node.left)
                if tmp_node.right:
                    queue.append(tmp_node.right)
        return depth


class Solution1:
    def getHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = self.getHeight(root.left)
        right_depth = self.getHeight(root.right)
        # 处理最小深度时，这里是一个关键,很容易想不到
        if root.left is None:
            return right_depth + 1
        if root.right is None:
            return left_depth + 1
        return min(left_depth, right_depth) + 1

    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        DFS，求高度，后序遍历
        :param root:
        :return:
        """
        return self.getHeight(root)
