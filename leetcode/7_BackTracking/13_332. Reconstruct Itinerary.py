#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: chao yang
@contact: cryoung777@gmail.com
@file: 13_332. Reconstruct Itinerary.py
@time: 2025/4/18 下午2:28
@desc:
"""
import copy
from typing import List


class Solution:
    def compare(self, one: List[str], two: List[str]) -> bool:
        """
        one的字典序是不是比two小
        :param one:
        :param two:
        :return:
        """
        for i in range(len(one)):
            if one[i] != two[i]:
                if one[i] < two[i]:
                    return True
                else:
                    return False
        return False

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        pass


if __name__ == '__main__':
    s = Solution()
    tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "JFK"], ["ATL", "AAA"], ["AAA", "ATL"], ["ATL", "BBB"],
               ["BBB", "ATL"], ["ATL", "CCC"], ["CCC", "ATL"], ["ATL", "DDD"], ["DDD", "ATL"], ["ATL", "EEE"],
               ["EEE", "ATL"], ["ATL", "FFF"], ["FFF", "ATL"], ["ATL", "GGG"], ["GGG", "ATL"], ["ATL", "HHH"],
               ["HHH", "ATL"], ["ATL", "III"], ["III", "ATL"], ["ATL", "JJJ"], ["JJJ", "ATL"], ["ATL", "KKK"],
               ["KKK", "ATL"], ["ATL", "LLL"], ["LLL", "ATL"], ["ATL", "MMM"], ["MMM", "ATL"], ["ATL", "NNN"],
               ["NNN", "ATL"]]
    print(s.findItinerary(tickets))
