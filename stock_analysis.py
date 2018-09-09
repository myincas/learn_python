#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 20:28:34 2017

@author: shixiaobin
"""

import tushare as ts
import pandas as pd

industry = ts.get_industry_classified()
concept = ts.get_concept_classified()

industry.c_name.unique()
concept.c_name.unique()

medical = industry[industry.c_name == '医疗器械']

stock_infos = ts.get_stock_basics()
medical_infos = stock_infos[stock_infos.index.isin(medical.code)]

a = "\Virtual Disks\DG2_ASM04\ACTIVE"
a.split('\\')[-2]

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, ' ')
        a, b = b, a + b
    print()


new_list = [range(1), range(2), range(3)]
[sum(i) for i in new_list]
newer_list = []
newer_list.append([sum(i) for i in new_list])
