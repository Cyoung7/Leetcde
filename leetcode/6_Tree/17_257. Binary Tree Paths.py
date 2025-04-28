#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 17_257. Binary Tree Paths.py
@time: 2025/4/15 下午1:12
@desc:
"""
import collections
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        DFS，前序遍历
        :param root:
        :return:
        """
        values = list()

        def dfs(d_root, path):
            new_path = "{}->{}".format(path, d_root.val) if path != "" else "{}".format(d_root.val)
            if d_root.left is None and d_root.right is None:
                values.append(new_path)
                return
            if d_root.left:
                dfs(d_root.left, new_path)
            if d_root.right:
                dfs(d_root.right, new_path)
            return

        dfs(root, "")
        return values



class Solution1:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        迭代法实现dfs，遍历顺序是中右左
        :param root:
        :return:
        """
        stack = list()
        path_st = list()
        result = list()
        if root:
            stack.append(root)
            path_st.append(str(root.val))
        while stack:
            tmp_node = stack.pop()
            tmp_path = path_st.pop()
            if tmp_node.left is None and tmp_node.right is None:
                result.append(tmp_path)
            if tmp_node.left:
                stack.append(tmp_node.left)
                path_st.append("{}->{}".format(tmp_path, tmp_node.left.val))
            if tmp_node.right:
                stack.append(tmp_node.right)
                path_st.append("{}->{}".format(tmp_path, tmp_node.right.val))
        return result


if __name__ == '__main__':
    s = Solution()
    r = TreeNode(1)
    print(s.binaryTreePaths(r))