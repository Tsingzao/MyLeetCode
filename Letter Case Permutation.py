# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 13:25:16 2018

@author: Tsingzao
"""

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        temp = [[i.lower(),i.upper()] if i.isalpha() else i for i in S]
        return [''.join(i) for i in itertools.product(*temp)]
        