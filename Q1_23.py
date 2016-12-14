#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 16:47:22 2016

@author: sethstrimas-mackey

Q1_23 All of Statistics
"""

import matplotlib.pyplot as plt
import random
import sys
import numpy as np

def main():
    
    n = 1000000
    
    A = [2, 4, 6]
    B = [1, 2, 3, 4]
    AB = [2, 4]
    
    N_a, N_b, N_ab = 0, 0, 0
    
    samples = np.random.randint(1, 7, size = n)
    
    for x in samples:
        if x in A:
            N_a += 1
            if x in AB:
                N_ab += 1
        if x in B:
            N_b += 1
            
    
    sim = N_a*N_b/n**2
    exp = N_ab/n
    
    print(sim, exp)
        
if __name__ == '__main__':
    main()