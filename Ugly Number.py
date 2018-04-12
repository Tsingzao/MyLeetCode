# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 09:24:58 2018

@author: Tsingzao
"""

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        if num == 1:
            return True
        while num != 2 and num != 3 and num != 5:
            if num % 2 == 0:
                num = num / 2
                continue
            if num % 3 == 0:
                num = num / 3
                continue
            if num % 5 == 0:
                num = num / 5
                continue
            return False
        return True