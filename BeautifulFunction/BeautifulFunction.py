#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 09:08:43 2021

@author: samac
"""

#declaring global variables count and lst

#to keep track of rechable numbers
count=0

#to store all the rechable number
lst=[]


def BeautifulFunction(x):
    #calling global variables lat and count 
    global lst,count
    if x in lst:
        #once a number is repeated in lst print count and return
        print(count)
        return
    else:
        #add the number to list lst
        lst.append(x)
        x=x+1
        #we need to perform strip function which is only possible for string so we convert our integer to string
        x=str(x)
        #remove the 0's at end or start of the string
        x=x.strip("0")
        #convert back to integer
        x=int(x)
        count=count+1
        BeautifulFunction(x)
        

BeautifulFunction(int(input()))
