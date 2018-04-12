# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 13:09:19 2018

@author: Tsingzao
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = 1
        while abs(s * s - x) > 0.0001:
            s = (s + x/s)/2.
        return int(s)