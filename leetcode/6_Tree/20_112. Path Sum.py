#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 20_112. Path Sum.py
@time: 2025/4/15 下午8:26
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        dfs：后序遍历
        :param root:
        :param targetSum:
        :return:
        """
        def dfs(node: Optional[TreeNode], tmp_sum) -> bool:
            nonlocal targetSum
            if node.left is None and node.right is None:
                return tmp_sum + node.val == targetSum
            left_success = dfs(node.left, tmp_sum+node.val) if node.left else False
            right_success = dfs(node.right, tmp_sum+node.val) if node.right else False
            return left_success or right_success
        if root:
            return dfs(root, 0)
        return False

    def hasPathSum_2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        dfs：后序遍历
        :param root:
        :param targetSum:
        :return:
        """
        def dfs(node: Optional[TreeNode], tmp_sum) -> bool:
            nonlocal targetSum
            if node is None:
                return tmp_sum == targetSum
            # 这道题和12_111是一样的，要特殊特里左右子树可能为None的非叶子节点
            if node.left is None:
                return dfs(node.right, tmp_sum+node.val)
            if node.right is None:
                return dfs(node.left, tmp_sum+node.val)
            left_success = dfs(node.left, tmp_sum+node.val)
            right_success = dfs(node.right, tmp_sum+node.val)
            return left_success or right_success
        if root:
            return dfs(root, 0)
        return False


class Solution1:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        迭代法实现dfs
        :param root:
        :param targetSum:
        :return:
        """
        stack = list()
        if root:
            stack.append((root, root.val))
        while stack:
            tmp_node, tmp_sum = stack.pop()
            if tmp_node.left is None and tmp_node.right is None and tmp_sum == targetSum:
                return True
            if tmp_node.left:
                stack.append((tmp_node.left, tmp_sum + tmp_node.left.val))
            if tmp_node.right:
                stack.append((tmp_node.right, tmp_sum + tmp_node.right.val))
        return False
