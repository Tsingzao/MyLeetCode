# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 10:27:20 2018

@author: Tsingzao
"""

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        temp = bin(num)
        temp = temp[2:]
        ones = temp.count('1')
        if ones > 1:
            return False
        else:
            if temp.count('0') % 2 == 0:
                return True
        return False