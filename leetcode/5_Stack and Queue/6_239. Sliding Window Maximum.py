#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 6_239. Sliding Window Maximum.py
@time: 2025/4/12 上午10:42
@desc:
"""
import math
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        超时
        :param nums:
        :param k:
        :return:
        """
        q = deque()
        result: List[int] = list()
        tmp_max = -math.inf
        pre_pop = None
        for num in nums:
            q.append(num)
            if len(q) == k:
                if num > tmp_max:
                    result.append(num)
                    tmp_max = num
                elif pre_pop != tmp_max:
                    result.append(tmp_max)
                else:
                    tmp_max = max(q)
                    result.append(tmp_max)
                pre_pop = q.popleft()
            else:
                tmp_max = max(num, tmp_max)
        return result


class MyQueue:  # 单调队列（从大到小
    def __init__(self):
        self.queue = deque()  # 这里需要使用deque实现单调队列，直接使用list会超时

    # 每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。
    # 同时pop之前判断队列当前是否为空。
    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()  # list.pop()时间复杂度为O(n),这里需要使用collections.deque()

    # 如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。
    # 这样就保持了队列里的数值是单调从大到小的了。
    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    # 查询当前队列里的最大值 直接返回队列前端也就是front就可以了。
    def front(self):
        return self.queue[0]


class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        核心思想：维护一个单调队列，每次直接从头部取出最大值
        :param nums:
        :param k:
        :return:
        """
        que = MyQueue()
        result = []
        for i in range(k):  # 先将前k的元素放进队列
            que.push(nums[i])
        result.append(que.front())  # result 记录前k的元素的最大值
        for i in range(k, len(nums)):
            que.pop(nums[i - k])  # 滑动窗口移除最前面元素
            que.push(nums[i])  # 滑动窗口前加入最后面的元素
            result.append(que.front())  # 记录对应的最大值
        return result


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(s.maxSlidingWindow(nums, k))