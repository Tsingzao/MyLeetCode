# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 13:25:20 2018

@author: Tsingzao
"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n > 0:
            n = n // 5
            cnt = cnt + n
        return cnt