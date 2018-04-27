# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 14:37:13 2018

@author: Tsingzao
"""
       
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 1:
            return 1
        idx = 0
        index = 0
        while idx < len(chars):
            char = chars[idx]
            cnt = 0
            while idx < len(chars) and chars[idx] == char:
                idx += 1
                cnt += 1
            chars[index] = char
            index += 1
            if not cnt == 1:
                cnt = str(cnt)
                for j in cnt:
                    chars[index] = j
                    index += 1
        return index