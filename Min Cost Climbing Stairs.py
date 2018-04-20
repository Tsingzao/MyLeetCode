# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:57:22 2018

@author: Tsingzao
"""

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        min0, min1 = cost[0], cost[1]
        for i in range(2, len(cost)):
            min0, min1 = min1, min(min0,min1)+cost[i]
        return min(min0,min1)