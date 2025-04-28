#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 18_404. Sum of Left Leaves.py
@time: 2025/4/15 下午7:44
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
    def dfs(self, node: Optional[TreeNode], is_left) -> int:
        """
        dfs: 后序遍历
        :param node:
        :param is_left:
        :return:
        """

        if node.left is None and node.right is None:
            return node.val if is_left else 0
        left_sum = self.dfs(node.left, True) if node.left else 0
        right_sum = self.dfs(node.right, False) if node.right else 0
        return left_sum + right_sum

    def dfs_2(self, node: Optional[TreeNode], is_left) -> int:
        """
        dfs: 后序遍历
        :param node:
        :param is_left:
        :return:
        """
        # 将空节点的作为递归的结束状态
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return node.val if is_left else 0

        left_sum = self.dfs(node.left, True)
        right_sum = self.dfs(node.right, False)
        return left_sum + right_sum

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, False)
