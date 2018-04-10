# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 14:55:47 2018

@author: Tsingzao
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s)) != len(set(t)):
            return False
        else:
            key_value = {}
            for i in range(len(s)):
                if not s[i] in key_value:
                    key_value[s[i]] = t[i]
                else:
                    if key_value[s[i]] != t[i]:
                        return False
            return True