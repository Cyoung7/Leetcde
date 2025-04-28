#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 11_Complete Knapsack.py
@time: 2025/4/23 下午3:31
@desc:https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E8%83%8C%E5%8C%85%E9%97%AE%E9%A2%98%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80%E5%AE%8C%E5%85%A8%E8%83%8C%E5%8C%85.md
和01背包主要区别：
递推公式：
dp[i][j] = max(dp[i - 1][j], dp[i][j - weight[i]] + value[i]);
01背包中是 dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
初始化：第一行，容量够，就一直装，而不是只装一个
"""


def knapsack(n, bag_weight, weight, value):
    dp = [[0] * (bag_weight + 1) for _ in range(n)]

    # 初始化
    for j in range(weight[0], bag_weight + 1):
        dp[0][j] = dp[0][j - weight[0]] + value[0]

    # 动态规划
    for i in range(1, n):
        for j in range(bag_weight + 1):
            if j < weight[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - weight[i]] + value[i])

    return dp[n - 1][bag_weight]

def complete_knapsack(N, bag_weight, weight, value):
    """
    dp一维数组的实现
    :param N:
    :param bag_weight:
    :param weight:
    :param value:
    :return:
    """
    dp = [0] * (bag_weight + 1)

    for j in range(bag_weight + 1):  # 遍历背包容量
        for i in range(len(weight)):  # 遍历物品
            if j >= weight[i]:
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    return dp[bag_weight]


if __name__ == '__main__':

    # 输入
    n, bag_weight = map(int, input().split())
    weight = []
    value = []
    for _ in range(n):
        w, v = map(int, input().split())
        weight.append(w)
        value.append(v)

    # 输出结果
    print(knapsack(n, bag_weight, weight, value))
