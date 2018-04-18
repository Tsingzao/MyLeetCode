# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 09:14:12 2018

@author: Tsingzao
"""

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int('1'*(len(bin(num))-2),2)^num