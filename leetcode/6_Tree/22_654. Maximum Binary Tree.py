#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 22_654. Maximum Binary Tree.py
@time: 2025/4/15 下午8:57
@desc:
"""
import math
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        这个能不能改成迭代法?
        :param nums:
        :return:
        """
        if len(nums) == 0:
            return None
        # 按照最大值切割
        max_num = -math.inf
        max_idx = -1
        for idx, num in enumerate(nums):
            if num > max_num:
                max_num = num
                max_idx = idx
        # 递归构造
        left_node = self.constructMaximumBinaryTree(nums[0: max_idx])
        right_node = self.constructMaximumBinaryTree(nums[max_idx+1:])
        return TreeNode(max_num, left_node, right_node)
