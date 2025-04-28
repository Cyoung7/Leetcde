#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 34_538. Convert BST to Greater Tree.py
@time: 2025/4/16 下午3:53
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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        递归，中序遍历，右中左的遍历顺序
        :param root:
        :return:
        """
        sum_value = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal sum_value
            if node is None:
                return
            dfs(node.right)
            sum_value += node.val
            node.val = sum_value
            dfs(node.left)

        dfs(root)
        return root


class Solution1:
    def dfs(self, node: Optional[TreeNode], pre_sum: int) -> int:
        if node is None:
            return pre_sum
        right_sum = self.dfs(node.right, pre_sum)
        sum_value = right_sum + node.val
        node.val = sum_value
        return self.dfs(node.left, sum_value)

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        递归，不使用全局变量
        :param root:
        :return:
        """
        self.dfs(root, 0)
        return root


class Solution2:

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        迭代
        :param root:
        :return:
        """
        stack = list()
        pre_sum = 0
        if root:
            stack.append(root)
        while stack:
            tmp_node = stack.pop()
            if tmp_node is not None:
                if tmp_node.left:
                    stack.append(tmp_node.left)
                stack.append(tmp_node)
                stack.append(None)
                if tmp_node.right:
                    stack.append(tmp_node.right)
            else:
                tmp_node = stack.pop()
                pre_sum += tmp_node.val
                tmp_node.val = pre_sum
        return root
