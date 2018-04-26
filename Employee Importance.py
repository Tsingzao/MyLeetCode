# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 22:58:47 2018

@author: Tsingzao
"""

"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        emp = {employee.id: employee for employee in employees}
        def dfs(id):
            cum = sum(dfs(subid) for subid in emp[id].subordinates)
            return cum + emp[id].importance
        return dfs(id)