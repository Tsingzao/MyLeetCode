# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 14:55:32 2018

@author: Tsingzao
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])