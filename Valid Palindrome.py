# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 16:20:28 2018

@author: Tsingzao
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join(c for c in s if c.isalnum()).lower()
        l = 0
        r = len(s)-1
        while l<r:
            if s[l] != s[r]:
                return False
            l = l + 1
            r = r - 1
        return True
    