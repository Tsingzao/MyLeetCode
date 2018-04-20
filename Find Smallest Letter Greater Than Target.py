# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 15:22:16 2018

@author: Tsingzao
"""

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        bias = 30
        urg = 0
        for letter in letters:
            if ord(letter)-ord(target)>0:
                bias = min(bias, ord(letter)-ord(target))
            else:
                urg = max(urg, ord(target)-ord(letter))
        if bias != 30:    
            return chr(bias+ord(target))
        else:
            return chr(ord(target)-urg)