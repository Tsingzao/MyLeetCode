# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 13:06:44 2018

@author: Tsingzao
"""

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        for ban in banned+['!','?','\'',',',';','.']:
            paragraph = paragraph.replace(ban,"")
        paragraph = paragraph.replace("  "," ")
        key_word = {}
        for word in paragraph.split(' '):
            if word == '':
                continue
            if word in key_word:
                key_word[word] = key_word[word] + 1
            else:
                key_word[word] = 1
        fre_cnt = 0
        fre_word= ""
        for key in key_word:
            if key_word[key] > fre_cnt:
                fre_word = key
                fre_cnt = key_word[key]
        return fre_word