# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 14:50:35 2018

@author: Tsingzao
"""

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        C = ""
        for i in range(len(B)/len(A)+3):
            if B in C:
                return i
            C = C + A
        return -1