# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 22:39:49 2018

@author: Tsingzao
"""

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        h = m
        w = n
        for op in ops:
            h = h if op[0] > h else op[0]
            w = w if op[1] > w else op[1]
        return h*w