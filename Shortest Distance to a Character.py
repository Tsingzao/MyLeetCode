# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 22:58:44 2018

@author: Tsingzao
"""

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n = len(S)
        ret = [n] * n
        pos = -n
        for i in range(n):
            if S[i] == C:
                pos = i
            ret[i] = min(ret[i], abs(i - pos))
        for i in range(n-1, -1, -1):
            if S[i] == C:
                pos = i
            ret[i] = min(ret[i], abs(i - pos))
        return ret