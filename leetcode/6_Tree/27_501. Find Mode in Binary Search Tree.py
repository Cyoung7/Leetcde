#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 27_501. Find Mode in Binary Search Tree.py
@time: 2025/4/16 上午10:57
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
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        """
        使用迭代法的中序遍历
        :param root:
        :return:
        """
        stack = list()
        # 记录最大出现结果
        results = list()
        # 记录最大出现次数
        max_count = -1

        # 保存前值
        pre_value = sys.maxsize
        # 临时计数
        count = 0

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
                # 还是利用二叉搜索树中序遍历有序的特点处理
                # 如果是普通树，直接全部遍历，用dict存储节点的统计频次，再排序
                if tmp_node.val != pre_value:
                    count = 1
                    pre_value = tmp_node.val
                else:
                    count += 1
                if count > max_count:
                    results.clear()
                    results.append(tmp_node.val)
                    max_count = count
                elif count == max_count:
                    results.append(tmp_node.val)
        return results
