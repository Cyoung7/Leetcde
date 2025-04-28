#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 21_106. Construct Binary Tree from Inorder and Postorder Traversal.py
@time: 2025/4/16 上午8:45
@desc:
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        node_num = len(inorder)
        if node_num == 0:
            return None
        root_val = postorder[-1]
        root_idx = inorder.index(root_val)

        # python list切片都是左闭右开区间
        left_tree = self.buildTree(inorder[0:root_idx], postorder[0:root_idx])
        right_tree = self.buildTree(inorder[root_idx+1:node_num], postorder[root_idx:node_num-1])
        return TreeNode(root_val, left_tree, right_tree)
