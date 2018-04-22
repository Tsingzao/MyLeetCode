# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 18:01:30 2018

@author: Tsingzao
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')