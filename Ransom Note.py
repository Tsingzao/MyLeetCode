# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 19:00:40 2018

@author: Tsingzao
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r = collections.Counter(ransomNote)
        m = collections.Counter(magazine)
        if r - m:
            return False
        else:
            return True