#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 31_450. Delete Node in a BST.py
@time: 2025/4/16 下午1:58
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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        教程里的迭代法更优雅一些
        https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0450.%E5%88%A0%E9%99%A4%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.md
        迭代法
        第一种情况：没找到删除的节点，遍历到空节点直接返回了
        找到删除的节点
        第二种情况：左右孩子都为空（叶子节点），直接删除节点， 返回NULL为根节点
        第三种情况：删除节点的左孩子为空，右孩子不为空，删除节点，右孩子补位，返回右孩子为根节点
        第四种情况：删除节点的右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
        第五种情况：左右孩子节点都不为空，则将删除节点的左子树头结点（左孩子）放到删除节点的右子树的最左面节点的左孩子上，返回删除节点右孩子为新的根节点。
        :param root:
        :param key:
        :return:
        """
        if root is None:
            return None
        tmp_node = root
        pre_node = None
        is_left = True
        while tmp_node:
            if tmp_node.val > key:
                pre_node = tmp_node
                is_left = True
                tmp_node = tmp_node.left
            elif tmp_node.val < key:
                pre_node = tmp_node
                tmp_node = tmp_node.right
                is_left = False
            else:
                if tmp_node.left is None and tmp_node.right is None:
                    if pre_node is None:
                        return None
                    if is_left:
                        pre_node.left = None
                    else:
                        pre_node.right = None
                    break
                elif tmp_node.left is None and tmp_node.right is not None:
                    if pre_node is None:
                        return root.right
                    if is_left:
                        pre_node.left = tmp_node.right
                    else:
                        pre_node.right = tmp_node.right
                    break
                elif tmp_node.right is None and tmp_node.left is not None:
                    if pre_node is None:
                        return root.left
                    if is_left:
                        pre_node.left = tmp_node.left
                    else:
                        pre_node.right = tmp_node.left
                    break
                else:
                    last_left = tmp_node.right
                    while last_left.left:
                        last_left = last_left.left
                    # 将待删除节点的左子树，添加到右子树最左面节点的左孩子上
                    last_left.left = tmp_node.left
                    if pre_node is None:
                        root = root.right
                    else:
                        if is_left:
                            pre_node.left = tmp_node.right
                        else:
                            pre_node.right = tmp_node.right
                    break
        return root


class Solution1:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        递归
        :param root:
        :param key:
        :return:
        """
        if root is None:
            return None
        if root.val == key:
            if root.left is None and root.right is None:
                return None
            elif root.left is None and root.right is not None:
                return root.right
            elif root.left is not None and root.right is None:
                return root.left
            else:
                tmp_node = root.right
                while tmp_node.left:
                    tmp_node = tmp_node.left
                # 将待删除节点的左子树，添加到右子树最左面节点的左孩子上
                tmp_node.left = root.left
                return root.right
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
