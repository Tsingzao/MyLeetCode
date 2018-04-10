# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:56:21 2018

@author: Tsingzao
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        c = collections.Counter(s)
        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
        return -1

