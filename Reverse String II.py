# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 19:18:52 2018

@author: Tsingzao
"""

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in xrange(0, len(s), 2*k):
            s[i:i+k] = s[i:i+k][::-1]
        return "".join(s)