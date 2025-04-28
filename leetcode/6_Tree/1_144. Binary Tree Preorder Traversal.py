#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 1_144. Binary Tree Preorder Traversal.py
@time: 2025/4/14 下午2:25
@desc:
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        核心思想：前序遍历，先遍历父节点，再遍历左右子节点
        递归，深度优先搜索
        :param root:
        :return:
        """
        value = list()
        if root is None:
            return value
        value.append(root.val)
        value.extend(self.preorderTraversal(root.left))
        value.extend(self.preorderTraversal(root.right))
        return value


class Solution1:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        核心思想：迭代法实现前序遍历，利用栈来代替递归实现
        :param root:
        :return:
        """
        stack = list()
        if root is not None:
            stack.append(root)
        value = list()
        while len(stack) > 0:
            tmp_node = stack.pop()
            value.append(tmp_node.val)
            if tmp_node.right is not None:
                stack.append(tmp_node.right)
            if tmp_node.left is not None:
                stack.append(tmp_node.left)
        return value


class Solution2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        核心思想：迭代法,空指针标记法
        :param root:
        :return:
        """
        stack = list()
        value = list()

        if root is not None:
            stack.append(root)

        while stack:
            tmp_node = stack.pop()
            if tmp_node is not None:
                # 前序遍历顺序为 中左右，所以入栈顺序为右左中
                if tmp_node.right:
                    stack.append(tmp_node.right)
                if tmp_node.left:
                    stack.append(tmp_node.left)
                # 对需要处理的节点用空指针标记
                stack.append(tmp_node)
                stack.append(None)
            else:
                # 遇到空指针，处理节点数据
                tmp_node = stack.pop()
                value.append(tmp_node.val)
        return value


class Solution3:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        核心思想：迭代法,boolean标记法
        :param root:
        :return:
        """
        stack = list()
        value = list()

        if root is not None:
            stack.append((root, False))

        while stack:
            tmp_node, is_visited = stack.pop()
            if is_visited:
                value.append(tmp_node.val)
                continue

            if tmp_node.right:
                stack.append((tmp_node.right, False))
            if tmp_node.left:
                stack.append((tmp_node.left, False))
            # 对需要处理的节点用空指针标记
            stack.append((tmp_node, True))

        return value
