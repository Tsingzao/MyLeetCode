# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 14:25:01 2018

@author: Tsingzao
"""

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        temp = 0 
        for i in range(1,int(num**(0.5))+1):
            if num % i == 0:
                temp = temp + i + num / i
        return temp == num*2