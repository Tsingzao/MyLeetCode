# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 15:07:35 2018

@author: Tsingzao
"""

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        cnt = 0
        for num in range(1,N+1):
            num = str(num)
            if '3' in num or '4' in num or '7' in num:
                continue
            if '2' in num or '5' in num or '6' in num or '9' in num:
                cnt = cnt + 1
        return cnt