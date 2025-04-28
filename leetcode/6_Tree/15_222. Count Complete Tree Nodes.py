#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 15_222. Count Complete Tree Nodes.py
@time: 2025/4/15 上午10:37
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        最朴素的方法，BFS计数每个节点
        :param root:
        :return:
        """
        if root is None:
            return 0
        queue = collections.deque()
        queue.append(root)
        count = 0
        while queue:
            tmp_node = queue.popleft()
            count += 1
            if tmp_node.left:
                queue.append(tmp_node.left)
            if tmp_node.right:
                queue.append(tmp_node.right)
        return count


class Solution1:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        朴素的递归
        :param root:
        :return:
        """
        if root is None:
            return 0
        left_count = self.countNodes(root.left)
        right_count = self.countNodes(root.right)
        return left_count + right_count + 1


class Solution2:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        利用完全二叉树的特性，寻找左右子树深度相同的满二叉树
        :param root:
        :return:
        """
        if root is None:
            return 0
        left_node = root.left
        right_node = root.right
        depth = 1
        while left_node and right_node:
            depth += 1
            left_node = left_node.left
            right_node = right_node.right

        if left_node is None and right_node is None:
            return 2 ** depth - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1


class Solution3:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        用迭代法实现完全二叉树特性
        :param root:
        :return:
        """
        pass
