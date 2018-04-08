# -*- coding: utf-8 -*-
"""
Created on Sun Apr 08 18:52:41 2018

@author: Tsingzao
"""

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits)-1:
            if bits[i] == 1:
                i = i + 2
            else:
                i = i + 1
        return i == len(bits)-1