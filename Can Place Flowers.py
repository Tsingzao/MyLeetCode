# -*- coding: utf-8 -*-
"""
Created on Thu Apr 05 18:52:07 2018

@author: Tsingzao
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        ss = ''.join(map(str,flowerbed))
        s = ss.replace('010','xxx').replace('10','xx').replace('01','xx').replace('00','0x')
        return s.count('0')>=n