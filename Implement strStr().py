# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 16:15:41 2018

@author: Tsingzao
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1