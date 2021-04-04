#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 09:08:43 2021

@author: samac
"""

count=0
lst=[]


def BeautifulFunction(x):
    global lst,count
    if x in lst:
        print(count)
        return
    else:
        lst.append(x)
        x=x+1
        x=str(x)
        x=x.strip("0")
        x=int(x)
        count=count+1
        BeautifulFunction(x)
        

BeautifulFunction(int(input()))