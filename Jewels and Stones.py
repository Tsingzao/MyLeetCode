# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:42:18 2018

@author: Tsingzao
"""

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        c = collections.Counter(S)
        temp = 0
        for jj in J:
            temp = temp + c[jj]
        return temp