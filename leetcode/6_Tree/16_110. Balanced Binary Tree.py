#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 16_110. Balanced Binary Tree.py
@time: 2025/4/15 上午11:09
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
    def getHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_height = self.getHeight(root.left)
        # -1作为标记不平衡高度，这个是关键
        if left_height == -1:
            return -1
        right_height = self.getHeight(root.right)
        if right_height == -1:
            return -1
        return -1 if abs(left_height - right_height) > 1 else max(left_height, right_height) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        求高度就得后序遍历
        求深度就用前序遍历
        :param root:
        :return:
        """
        return False if self.getHeight(root) == -1 else True

