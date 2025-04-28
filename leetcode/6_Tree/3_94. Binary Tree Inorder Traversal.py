#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 3_94. Binary Tree Inorder Traversal.py
@time: 2025/4/14 下午2:35
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        核心思想：中序遍历，先遍历左节点，再遍历父节点，最后遍历右节点
        :param root:
        :return:
        """
        value = list()
        if root is None:
            return value
        value.extend(self.inorderTraversal(root.left))
        value.append(root.val)
        value.extend(self.inorderTraversal(root.right))
        return value


class Solution1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        核心思想：迭代法实现中序遍历，先把父节点全部压栈，取值，再遍历右节点
        中序遍历区别与前序和后序遍历

        在使用迭代法写中序遍历，就需要借用指针的遍历来帮助访问节点，栈则用来处理节点上的元素
        :param root:
        :return:
        """
        stack = list()
        value = list()

        cur = root
        while cur is not None or len(stack) > 0:
            if cur is not None:
                # 指针的遍历来帮助访问节点
                stack.append(cur)
                cur = cur.left
            else:
                # 栈则用来处理节点上的元素
                cur = stack.pop()
                value.append(cur.val)
                cur = cur.right
        return value


class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        核心思想：迭代法,空指针标记法
        :param root:
        :return:
        """
        stack = list()
        value = list()
        if root:
            stack.append(root)
        while stack:
            tmp_node = stack.pop()
            if tmp_node is not None:
                if tmp_node.right:
                    stack.append(tmp_node.right)
                stack.append(tmp_node)
                stack.append(None)
                if tmp_node.left:
                    stack.append(tmp_node.left)
            else:
                tmp_node = stack.pop()
                value.append(tmp_node.val)
        return value


class Solution3:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        核心思想：迭代法,boolean标记法
        :param root:
        :return:
        """
        stack = list()
        value = list()
        if root:
            stack.append((root, False))
        while stack:
            tmp_node, is_visited = stack.pop()
            if is_visited:
                value.append(tmp_node.val)
                continue
            if tmp_node.right:
                stack.append((tmp_node.right, False))
            stack.append((tmp_node, True))
            if tmp_node.left:
                stack.append((tmp_node.left, False))
        return value


# fuxi
class Solution4:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        value = list()
        stack = list()
        cur = root
        while cur is not None or len(stack):
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                value.append(cur.val)
                stack.append(cur.right)
        return value
