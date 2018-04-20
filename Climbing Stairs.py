# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 14:04:19 2018

@author: Tsingzao
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n
        else:
            a = 2
            b = 3
            for i in range(4,n+1):
                temp = a
                a = b
                b = temp + a
        return b