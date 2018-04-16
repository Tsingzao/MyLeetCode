# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 17:04:08 2018

@author: Tsingzao
"""

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        for key in s.split(' '):
            if key:
                cnt = cnt + 1
        return cnt
