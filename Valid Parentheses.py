# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 17:57:15 2018

@author: Tsingzao
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sk = []
        key_value = {')':'(',']':'[','}':'{'}
        for ss in s:
            if ss in key_value.values():
                sk.append(ss)
            else:
                if sk == [] or key_value[ss] != sk.pop():
                    return False
        return sk == []