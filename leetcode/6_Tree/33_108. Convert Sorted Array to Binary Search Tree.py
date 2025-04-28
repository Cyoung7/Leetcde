#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 33_108. Convert Sorted Array to Binary Search Tree.py
@time: 2025/4/16 下午3:33
@desc:
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        这一题和题22_654构造最大二叉树一个原理
        这一题选中间节点，使得树的两边节点适量不超过1，构造出来自然是平衡二叉树
        列表有序，自然满足左边小，右边大，满足二叉搜索树
        :param nums:
        :return:
        """
        if len(nums) == 0:
            return None
        num_len = len(nums)
        mid_idx = int(num_len / 2)
        left_tree = self.sortedArrayToBST(nums[:mid_idx])
        right_tree = self.sortedArrayToBST(nums[mid_idx+1:])
        return TreeNode(nums[mid_idx], left_tree, right_tree)


class Solution1:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        迭代法
        :param nums:
        :return:
        """
        pass
