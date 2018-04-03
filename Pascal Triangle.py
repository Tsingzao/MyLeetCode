# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 16:30:58 2018

@author: Tsingzao
"""

numRows = 5

bol = [[1],[1,1]]
for i in range(2, numRows):
    temp = [1]
    for j in range(i-1):
        temp.append(bol[i-1][j]+bol[i-1][j+1])
    temp.append(1)
    bol.append(temp)
print bol