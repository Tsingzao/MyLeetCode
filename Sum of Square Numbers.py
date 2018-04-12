# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 14:35:37 2018

@author: Tsingzao
"""

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(int(c**(0.5))+1):
            if int((c - i*i)**(0.5))**2+i*i == c:
                return True
        return False