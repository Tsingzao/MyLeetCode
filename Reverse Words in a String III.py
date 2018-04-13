# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:53:36 2018

@author: Tsingzao
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = []
        for word in s.split(' '):
            ret.append(word[::-1]+' ')
        return "".join(ret)[:-1]