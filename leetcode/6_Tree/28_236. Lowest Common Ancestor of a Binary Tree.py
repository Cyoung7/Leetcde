#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 28_236. Lowest Common Ancestor of a Binary Tree.py
@time: 2025/4/16 上午11:11
@desc:
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        公共祖先问题，还是有难度的
        主要思考如下几点：
            如何从底向上遍历？ 后序遍历
            遍历整棵树，还是遍历局部树？
            如何把结果传到根节点的？
        后序遍历，这道题还是很抽象的，需要多理解
        :param root:
        :param p:
        :param q:
        :return:
        """
        if root is p or root is q:
            return root

        left_node = self.lowestCommonAncestor(root.left, p, q) if root.left else None
        right_node = self.lowestCommonAncestor(root.right, p, q) if root.right else None
        # 说明两边都搜索到了节点
        if left_node is not None and right_node is not None:
            return root
        # 只搜索到一个节点
        elif left_node is None and right_node is not None:
            return right_node
        elif left_node is not None and right_node is None:
            return left_node
        else:
            return None


class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is p or root is q or root is None:
            return root

        left_node = self.lowestCommonAncestor(root.left, p, q)
        right_node = self.lowestCommonAncestor(root.right, p, q)
        # 说明两边都搜索到了节点
        if left_node is not None and right_node is not None:
            return root
        # 只搜索到一个节点
        elif left_node is None and right_node is not None:
            return right_node
        elif left_node is not None and right_node is None:
            return left_node
