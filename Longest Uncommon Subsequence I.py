# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 11:08:50 2018

@author: Tsingzao
"""

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        return max(len(a),len(b))