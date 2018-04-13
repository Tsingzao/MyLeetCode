# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 12:49:18 2018

@author: Tsingzao
"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 2:
            return True
        if ord(word[0]) >= 65 and ord(word[0]) <= 90:
            if ord(word[1]) >= 65 and ord(word[1]) <= 90:
                if len(word) == 2:
                    return True
                else:
                    for s in word[2:]:
                        if ord(s) > 90:
                            return False
                    return True
            else:
                if len(word) == 2:
                    return True
                else:
                    for s in word[2:]:
                        if ord(s) < 97:
                            return False
                    return True                
        else:
            for s in word[1:]:
                if ord(s) < 97:
                    return False
            return True
        '''===================hehe========================='''
        return word[1:]==word[1:].lower() or word==word.upper()