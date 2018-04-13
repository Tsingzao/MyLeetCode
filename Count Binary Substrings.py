# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 14:49:18 2018

@author: Tsingzao
"""

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = map(len, s.replace('01', '0 1').replace('10', '1 0').split())
        return sum(min(a, b) for a, b in zip(s, s[1:]))