# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:30:12 2018

@author: Tsingzao
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(' ')
        if len(pattern) != len(str):
            return False
        elif len(set(pattern)) != len(set(str)):
            return False
        else:
            key_value = {}
            for i in range(len(pattern)):
                if not pattern[i] in key_value:
                    key_value[pattern[i]] = str[i]
                else:
                    if key_value[pattern[i]] != str[i]:
                        return False
            return True
        
#==============================================================================
#         s = pattern
#         t = str.split()
#         return map(s.find, s) == map(t.index, t)
#==============================================================================
