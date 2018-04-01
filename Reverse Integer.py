# -*- coding: utf-8 -*-
"""
Created on Sun Apr 01 18:11:11 2018

@author: Tsingzao
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0 and int(str(-x)[::-1])*(-1)>-2**31:
            return int(str(-x)[::-1])*(-1)
        elif x>0 and int(str(x)[::-1])<2**31-1:
            return int(str(x)[::-1])
        else:
            return 0