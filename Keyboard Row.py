# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:39:07 2018

@author: Tsingzao
"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        l1, l2, l3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        r = []
        for word in words:
            w = set(word.lower())
            if w.issubset(l1) or w.issubset(l2) or w.issubset(l3):
                r.append(word)
        return r