# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 13:14:01 2018

@author: Tsingzao
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while num > 0:
            num = num - i
            i = i + 2
        if num == 0:
            return True
        return False