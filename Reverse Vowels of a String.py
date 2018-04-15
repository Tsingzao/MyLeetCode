# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 21:19:23 2018

@author: Tsingzao
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        lst = ['a','e','i','o','u','A','E','I','O','U']
        idx = []
        temp = []
        for i in range(len(s)):
            if s[i] in lst:
                idx.append(i)
                temp.append(s[i])
        temp = temp[::-1]
        for i in range(len(idx)):
            s[idx[i]] = temp[i]
        return "".join(s)