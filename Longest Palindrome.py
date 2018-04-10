# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 16:48:43 2018

@author: Tsingzao
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(set(s)) == 1:
            return len(s)
        c = collections.Counter(s)
        t = 0
        flag = False
        for key in c:
            if c[key] == 1:
                if not flag:
                    t = t + 1
                    flag = True
            elif c[key] % 2 == 0:
                t = t + c[key]
            else:
                if flag:
                    t = t + c[key] - 1
                else:
                    t = t + c[key]
                    flag = True
        return t