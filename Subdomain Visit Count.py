# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:53:22 2018

@author: Tsingzao
"""

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        key_value = {}
        for domain in cpdomains:
            click = int(domain.split(' ')[0])
            dom = domain.split(' ')[1].split('.')
            for i in range(len(dom)):
                d = ".".join(dom[i:])
                if not d in key_value:
                    key_value[d] = click
                else:
                    key_value[d] = click + key_value[d]
        r = []
        for key in key_value:
            r.append(str(key_value[key])+' '+key)
        return r