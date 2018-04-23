# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 16:09:16 2018

@author: Tsingzao
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n)[2:].zfill(32)[::-1],2)