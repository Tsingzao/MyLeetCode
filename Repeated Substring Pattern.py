# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 08:56:44 2018

@author: Tsingzao
"""

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s+s)[1:-1]