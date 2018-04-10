# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 08:36:09 2018

@author: Tsingzao
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tmp = []
        while 1:
            temp = 0
            while n > 0:
                temp = (n%10)**2 + temp
                n = n // 10
            n = temp
            if temp == 1:
                return True
            elif temp in tmp:
                return False
            else:
                tmp.append(temp)