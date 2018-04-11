# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 21:03:23 2018

@author: Tsingzao
"""

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        if len(set(candies)) * 2 >= len(candies):
            return len(candies) // 2
        else:
            return len(set(candies))