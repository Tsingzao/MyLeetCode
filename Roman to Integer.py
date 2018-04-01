# -*- coding: utf-8 -*-
"""
Created on Sun Apr 01 18:17:36 2018

@author: Tsingzao
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = 0
        mp = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s)-1):
            if mp[s[i]]<mp[s[i+1]]:
                a = a - mp[s[i]]
            else:
                a = a + mp[s[i]]
        return a + mp[s[-1]]