#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:24:31 2018

@author: eugene
"""

from fb import fizzbuzz
import pytest


def test_fizzbuzz_returns_str():
    assert isinstance(fizzbuzz(1), str)



#parametrize - which values we want for num
#to avoid write separate functions for each separate num    
@pytest.mark.parametrize('num', [1, 2, 4, 7, 8, 11, 13, 14])  
def test_fizzbuzz_regular_returns_self(num):
    assert fizzbuzz(num) == str(num) 
    
    
    
    
@pytest.mark.parametrize('num', [3, 6, 9, 12])  
def test_fizzbuzz_3div_returns_fizz(num):
    assert fizzbuzz(num) == 'fizz'


@pytest.mark.parametrize('num', [5, 10])  
def test_fizzbuzz_5div_returns_fizz(num):
    assert fizzbuzz(num) == 'buzz'


@pytest.mark.parametrize('num', [15, 15000015])  
def test_fizzbuzz_3div_5div_returns_fizz(num):
    assert fizzbuzz(num) == 'fizzbuzz'       