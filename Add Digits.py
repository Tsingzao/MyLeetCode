# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 22:23:36 2018

@author: Tsingzao
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            temp = 0
            while num:
                temp = temp + num % 10
                num = num // 10
            num = temp
        return num