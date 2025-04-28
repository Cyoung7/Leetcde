#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 17_968. Binary Tree Cameras.py
@time: 2025/4/23 上午9:04
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

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        result = 0

        def traversal(cur: Optional[TreeNode]) -> int:
            """
            0：该节点无覆盖
            1：本节点有摄像头
            2：本节点有覆盖
            :param cur:
            :return:
            """
            nonlocal result
            if cur is None:
                return 2
            left = traversal(cur.left)
            right = traversal(cur.right)

            if left == 2 and right == 2:
                return 0
            elif left == 0 or right == 0:
                result += 1
                return 1
            elif left == 1 or right == 1:
                return 2
            return -1

        if traversal(root) == 0:
            result += 1
        return result
