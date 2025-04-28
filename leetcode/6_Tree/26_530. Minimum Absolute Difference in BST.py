#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 26_530. Minimum Absolute Difference in BST.py
@time: 2025/4/16 上午10:24
@desc:
"""
import math
import sys
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        使用迭代法的中序遍历
        :param root:
        :return:
        """
        stack = list()
        pre_value = None
        min_diff = sys.maxsize
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
                if pre_value is None:
                    pre_value = tmp_node.val
                else:
                    # 最小差值只会出现在相邻的两个节点
                    min_diff = tmp_node.val - pre_value if tmp_node.val - pre_value < min_diff else min_diff
                    pre_value = tmp_node.val
        return min_diff


class Solution1:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = sys.maxsize
        pre_value = None

        def dfs(node: Optional[TreeNode]):
            """
            使用递归的中序遍历
            :param node:
            :return:
            """
            nonlocal min_diff, pre_value
            if node is None:
                return
            dfs(node.left)
            # 处理中间节点
            if pre_value is not None:
                min_diff = node.val - pre_value if node.val - pre_value < min_diff else min_diff
            pre_value = node.val

            dfs(node.right)
            return

        dfs(root)
        return min_diff
