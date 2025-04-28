#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 23_617. Merge Two Binary Trees.py
@time: 2025/4/16 上午9:21
@desc:
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        dfs前序遍历: 最朴素的写法，遍历每个节点,
        :param root1:
        :param root2:
        :return:
        """
        if root1 is None and root2 is None:
            return None
        node_val = 0
        left_tree = None
        right_tree = None
        if root1 is not None and root2 is not None:
            node_val = root1.val + root2.val
            left_tree = self.mergeTrees(root1.left, root2.left)
            right_tree = self.mergeTrees(root1.right, root2.right)
        elif root1 is None:
            node_val = root2.val
            left_tree = self.mergeTrees(None, root2.left)
            right_tree = self.mergeTrees(None, root2.right)
        elif root2 is None:
            node_val = root1.val
            left_tree = self.mergeTrees(root1.left, None)
            right_tree = self.mergeTrees(root1.right, None)
        return TreeNode(node_val, left_tree, right_tree)


class Solution1:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        dfs: 直接前序遍历即可
        :param root1:
        :param root2:
        :return:
        """
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

