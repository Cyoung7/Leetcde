#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 30_701. Insert into a Binary Search Tree.py
@time: 2025/4/16 下午1:34
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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        迭代法
        不保证平衡，插入到符合条件的空叶子的地方，一定不会破环二叉搜索树的结构
        :param root:
        :param val:
        :return:
        """
        if root is None:
            return TreeNode(val)
        tmp_node = root
        while tmp_node:
            if tmp_node.val < val:
                if tmp_node.right is None:
                    tmp_node.right = TreeNode(val)
                    break
                else:
                    tmp_node = tmp_node.right
            if tmp_node.val > val:
                if tmp_node.left is None:
                    tmp_node.left = TreeNode(val)
                    break
                else:
                    tmp_node = tmp_node.left
        return root


class Solution1:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        递归
        :param root:
        :param val:
        :return:
        """
        if root is None:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
