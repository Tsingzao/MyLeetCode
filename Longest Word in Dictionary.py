# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 22:58:29 2018

@author: Tsingzao
"""

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        ret, res = '', {''}
        for word in sorted(words):
            if word[:-1] in res:
                res.add(word)
                ret = max(ret, word, key=len)
        return ret