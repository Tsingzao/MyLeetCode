# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 19:07:36 2018

@author: Tsingzao
"""

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c = collections.Counter(s)
        if 'LLL' in s:
            return False
        else:
            if c['A'] < 2:
                return True
            else:
                return False