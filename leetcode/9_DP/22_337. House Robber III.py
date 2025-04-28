#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 22_337. House Robber III.py
@time: 2025/4/24 下午12:19
@desc: 树形dp
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob_dfs(self,  cur: Optional[TreeNode]) -> List[int]:
        # dp[0]: 该节点不偷的最大值， dp[1]:该节点偷的最大值
        if cur is None:
            return [0, 0]
        left = self.rob_dfs(cur.left)
        right = self.rob_dfs(cur.right)
        # 偷父节点一定不能偷子节点
        var1 = cur.val + left[0] + right[0]
        # 不偷父节点，直接选子节点最大值相加
        var2 = max(left[0], left[1]) + max(right[0], right[1])
        return [var2, var1]

    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.rob_dfs(root))
