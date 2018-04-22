# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 17:57:39 2018

@author: Tsingzao
"""

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        hen = []
        if num == 0:
            return '0'
        if num < 0:
            num = num + 2**32
        if num > 0:
            while num > 0:
                hen.insert(0,ret[num%16])
                num = num // 16
            return "".join(hen)