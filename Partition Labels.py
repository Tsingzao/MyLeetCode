# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 14:59:20 2018

@author: Tsingzao
"""

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ret = []
        while S:
            i = 1
            while set(S[:i]) & set(S[i:]):
                i += 1
            ret.append(i)
            S = S[i:]
        return ret
    