# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 16:57:49 2018

@author: Tsingzao
"""

rowIndex = 3

bol = [1]
for i in range(1, rowIndex+1):
    bol = [1] + [bol[j-1]+bol[j] for j in range(1,i)] + [1]
print bol