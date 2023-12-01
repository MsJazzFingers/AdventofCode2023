# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 17:56:39 2023

@author: silvr
"""

import numpy as N

inputfiln = 'C:\\Users\\silvr\\Documents\\AdventofCode2023\\AdventofCode2023-1_input.txt'

inputfile = open(inputfiln,'r')
inputs = inputfile.readlines()
inputfile.close()

calvals = []
for i in inputs:
    nums = [x for x in i if x.isnumeric()]
    strsum = nums[0]+nums[-1]
    calvals.append(strsum)

print(inputs[:3])
print(calvals[:3])

calvals = N.array(calvals).astype(int)

calsum = N.sum(calvals)
print('Sum of all calibration values is {}'.format(calsum))