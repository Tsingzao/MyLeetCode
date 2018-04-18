# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 09:25:48 2018

@author: Tsingzao
"""

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b = bin(n)
        for i in range(2,len(b)-1):
            if b[i] != b[i+1]:
                continue
            else:
                return False
        return True