# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 14:29:52 2018

@author: Tsingzao
"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        while i < len(s) / 2 and s[i] == s[-(i+1)]:
            i = i + 1
        s = s[i:len(s)-i]
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]