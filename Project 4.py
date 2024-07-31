# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 14:50:51 2023

@author: Admin
"""

# my id
M = 65875

# initialize count to 0
count = 0 

# count all the numbers between 1 and M that are even (divisible by 2) and divisible by 3 also
for n in range(1,M+1):
  if (n % 2 == 0) and (n % 3 == 0) and (n % 5 == 0) and (n % 7 != 0):
    count += 1
    

# display output
print("count x 19:", count * 19)
print("count:", count)
print("M:", M)
