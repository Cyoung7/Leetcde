#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 14_101. Symmetric Tree.py
@time: 2025/4/15 上午9:35
@desc:
"""
import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def compare(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True
        elif left is not None and right is None:
            return False
        elif left is None and right is not None:
            return False
        elif left.val != right.val:
            return False
        # 左子树的遍历方式为右左中，右子树遍历顺序时左右中
        in_same = self.compare(left.right, right.left)
        out_same = self.compare(left.left, right.right)
        return in_same and out_same

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        后序遍历
        :param root:
        :return:
        """
        if root is None:
            return True
        return self.compare(root.left, root.right)


class Solution1:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        BFS，左子树从左往右，右子树从右往左
        :param root:
        :return:
        """
        if root is None:
            return True
        # 用队列，实现方式是广度优先搜索
        queue = collections.deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            left_node = queue.popleft()
            right_node = queue.popleft()
            if left_node is None and right_node is None:
                continue
            elif left_node is None and right_node is not None:
                return False
            elif left_node is not None and right_node is None:
                return False
            elif left_node.val != right_node.val:
                return False
            else:
                # 左子树从左往右，右子树从右往左
                queue.append(left_node.left)
                queue.append(right_node.right)
                queue.append(left_node.right)
                queue.append(right_node.left)
        return True


class Solution2:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        DFS：用栈+迭代法实现
        :param root:
        :return:
        """
        if root is None:
            return True
        # 用栈，实现方式是深度优先搜索
        stack = list()
        stack.append(root.right)
        stack.append(root.left)
        while stack:
            left_node = stack.pop()
            right_node = stack.pop()
            if left_node is None and right_node is None:
                continue
            elif left_node is None and right_node is not None:
                return False
            elif left_node is not None and right_node is None:
                return False
            elif left_node.val != right_node.val:
                return False
            else:
                # 左子树从左往右，右子树从右往左
                stack.append(left_node.left)
                stack.append(right_node.right)
                stack.append(left_node.right)
                stack.append(right_node.left)
        return True
