# -*- coding: utf-8 -*-
"""
Created on Sun Apr 01 18:16:53 2018

@author: Tsingzao
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return x-int(str(x)[::-1])==0 if x>-1 else False