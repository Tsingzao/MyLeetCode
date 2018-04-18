# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 08:56:58 2018

@author: Tsingzao
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return str(bin(x^y)).count('1')