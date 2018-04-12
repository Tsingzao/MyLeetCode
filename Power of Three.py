# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 09:13:50 2018

@author: Tsingzao
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n == round(n) and n != 1:
            n = n / 3.
        if n == 1:
            return True
        else:
            return False