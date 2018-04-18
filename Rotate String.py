# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:37:57 2018

@author: Tsingzao
"""

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        return B in 2*A