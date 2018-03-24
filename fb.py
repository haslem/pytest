#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:25:54 2018

@author: eugene
"""

def fizzbuzz(number):
    ret =''
    #if number % 15 == 0:
        #return 'fizzbuzz'
    if number % 3 == 0:
        ret += 'fizz'
    if number % 5 == 0:
        ret += 'buzz'
        
    #empty string is False    
    return ret or str(number)


