#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 32_669. Trim a Binary Search Tree.py
@time: 2025/4/16 下午2:56
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
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
        递归
        :param root:
        :param low:
        :param high:
        :return:
        """
        if root is None:
            return None
        # 这个条件可要可不要，要了提高一些剪枝效果
        # if root.val == low:
        #     root.left = None
        #     # 因为右子树还有可能出现比high还大的值
        #     root.right = self.trimBST(root.right, low, high)
        #     return root
        # if root.val == high:
        #     # 因为子树还有可能出现比low还小的值
        #     root.left = self.trimBST(root.left, low, high)
        #     root.right = None
        #     return root

        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root


class Solution1:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
         迭代法
        :param root:
        :param low:
        :param high:
        :return:
        """
        pass
