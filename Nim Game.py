# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 08:44:56 2018

@author: Tsingzao
"""

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4 != 0