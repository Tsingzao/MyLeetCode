# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 13:59:22 2018

@author: Tsingzao
"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(((1+8*n)**(0.5)-1) / 2)