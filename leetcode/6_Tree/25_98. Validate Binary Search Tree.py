#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 25_98. Validate Binary Search Tree.py
@time: 2025/4/16 上午9:54
@desc:
"""
import math
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = list()

        def dfs(node: Optional[TreeNode]):
            """
            二叉搜索树，中序遍历结果就是一个有序的数组
            :param node:
            :return:
            """
            nonlocal values
            if node is None:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)
            return

        dfs(root)
        for i in range(1, len(values)):
            if values[i-1] >= values[i]:
                return False
        return True


class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        max_value = -math.inf

        def dfs(node: Optional[TreeNode]) -> bool:
            """
            二叉搜索树，中序遍历结果就是一个有序的数组
            :param node:
            :return:
            """
            nonlocal max_value
            if node is None:
                return True
            is_left = dfs(node.left)
            if max_value < node.val:
                max_value = node.val
            else:
                return False
            is_right = dfs(node.right)
            return is_left and is_right

        return dfs(root)


class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        迭代法
        无论是递归还是迭代法，都只能使用中序遍历
        :param root:
        :return:
        """
        stack = list()
        max_value = -math.inf
        if root:
            stack.append(root)
        while stack:
            # 中序是 左中右，入栈顺序是 右中左
            tmp_node = stack.pop()
            if tmp_node is not None:
                if tmp_node.right:
                    stack.append(tmp_node.right)
                stack.append(tmp_node)
                # 空指针标记法
                stack.append(None)
                if tmp_node.left:
                    stack.append(tmp_node.left)
            else:
                tmp_node = stack.pop()
                if tmp_node.val > max_value:
                    max_value = tmp_node.val
                else:
                    return False
        return True


if __name__ == '__main__':
    s = Solution2()
    node = TreeNode(2)
    print(s.isValidBST(node))