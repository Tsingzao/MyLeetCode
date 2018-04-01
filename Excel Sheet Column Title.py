# -*- coding: utf-8 -*-
"""
Created on Sun Apr 01 18:19:15 2018

@author: Tsingzao
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        a = ''
        while n>0:
            a = chr((n-1)%26+ord('A'))+a
            n = (n-1) // 26
        return a