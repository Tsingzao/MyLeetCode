# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 22:31:31 2018

@author: Tsingzao
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for ss in s:
            num = (ord(ss) - ord('A') + 1) + num * 26
        return num