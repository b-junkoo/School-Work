# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:32:48 2020

@author: Jun
"""
count = 0
s = 'fobobooboobbbobbobobobobobpobobooq'
for ind in range(len(s)):
    if s[ind] + s[ind+1] + s[ind+2] == 'bob':
        count += 1
    if len(s) - (ind+1) == 2:
        break
print("Number of times bob occurs is:", count)

