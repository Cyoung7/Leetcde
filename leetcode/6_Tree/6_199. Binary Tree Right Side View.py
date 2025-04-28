#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 6_199. Binary Tree Right Side View.py
@time: 2025/4/14 下午5:19
@desc:
"""
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS层次遍历，记录每一层最后一个节点值
        :param root:
        :return:
        """
        queue = deque()
        value = list()
        if root:
            queue.append(root)
        while queue:
            q_len = len(queue)
            for i in range(q_len):
                tmp_node = queue.popleft()
                if tmp_node.left:
                    queue.append(tmp_node.left)
                if tmp_node.right:
                    queue.append(tmp_node.right)
                if i+1 == q_len:
                    value.append(tmp_node.val)
        return value
