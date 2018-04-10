# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:16:36 2018

@author: Tsingzao
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return collections.Counter(s) == collections.Counter(t)