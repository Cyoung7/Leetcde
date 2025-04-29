#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 8_01backpack.py
@time: 2025/4/23 下午1:34
@desc: 01背包问题模板
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E8%83%8C%E5%8C%85%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%8001%E8%83%8C%E5%8C%85-1.md
"""


def main():
    """
    01背包 dp二维数组写法
    :return:
    """
    n, bagweight = map(int, input().split())
    weight = list(map(int, input().split()))
    value = list(map(int, input().split()))
    #
    dp = [[0] * (bagweight + 1) for _ in range(n)]

    for j in range(weight[0], bagweight + 1):
        dp[0][j] = value[0]

    # 遍历物品
    for i in range(1, n):
        # 遍历背包的重量
        for j in range(bagweight + 1):
            if j < weight[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

    print(dp[n - 1][bagweight])


def main1():
    """
    01背包 dp一维数组写法
    :return:
    """
    n, bagweight = map(int, input().split())
    weight = list(map(int, input().split()))
    value = list(map(int, input().split()))

    dp = [0] * (bagweight + 1)  # 创建一个动态规划数组dp，初始值为0

    dp[0] = 0  # 初始化dp[0] = 0,背包容量为0，价值最大为0

    # 应该先遍历物品，如果遍历背包容量放在上一层，那么每个dp[j]就只会放入一个物品
    for i in range(n):
        # 重点:倒序遍历背包容量是为了保证物品i只被放入一次
        for j in range(bagweight, weight[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    print(dp[bagweight])


if __name__ == '__main__':
    main1()
