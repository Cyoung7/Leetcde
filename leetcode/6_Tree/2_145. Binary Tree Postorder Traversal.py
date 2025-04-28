#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 2_145. Binary Tree Postorder Traversal.py
@time: 2025/4/14 下午2:32
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        核心思想：后序遍历，先遍历左右子节点，再遍历父节点
        :param root:
        :return:
        """
        value = list()
        if root is None:
            return value
        value.extend(self.postorderTraversal(root.left))
        value.extend(self.postorderTraversal(root.right))
        value.append(root.val)
        return value


class Solution1:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        核心思想：后续遍历是左右中，先中序遍历中右左，再反转结果
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
            if tmp_node.left is not None:
                stack.append(tmp_node.left)
            if tmp_node.right is not None:
                stack.append(tmp_node.right)
        return value[::-1]


class Solution2:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
                # 后序遍历顺序为左右中，所以入栈顺序为中右左
                stack.append(tmp_node)
                stack.append(None)
                if tmp_node.right:
                    stack.append(tmp_node.right)
                if tmp_node.left:
                    stack.append(tmp_node.left)
            else:
                tmp_node = stack.pop()
                value.append(tmp_node.val)
        return value


class Solution3:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
            # 后序遍历顺序为左右中，所以入栈顺序为中右左
            stack.append((tmp_node, True))

            if tmp_node.right:
                stack.append((tmp_node.right, False))
            if tmp_node.left:
                stack.append((tmp_node.left, False))
        return value
