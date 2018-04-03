# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 09:38:15 2018

@author: Tsingzao
"""

digits=[9]
digits=digits[::-1]

for i in range(len(digits)):
    digits[i] = digits[i]+1
    if i!=len(digits)-1:
        if digits[i] == 10:
            digits[i] = 0
            continue
        else:
            break
    else:
        if digits[i] == 10:
            digits[i] = 0
            digits.append(1)
        else:
            break
print digits[::-1]