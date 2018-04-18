# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 15:21:33 2018

@author: Tsingzao
"""

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        lst = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ret = []
        for word in words:
            temp = []
            for w in word:
                temp.append(lst[ord(w)-ord('a')])
            temp = "".join(temp)
            ret.append(temp)
        tmp = []
        for temp in ret:
            if temp in tmp:
                continue
            else:
                tmp.append(temp)
        return len(tmp)