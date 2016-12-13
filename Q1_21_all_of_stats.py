#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:49:41 2016

@author: sethstrimas-mackey

All of Statistics, Q1.21
Suppose a coin has probability P of falling heads up. 
If we flip the coin many times, we would expect the proportion 
of heads to be near p. We will make this formal later. 
Take P = .3 and n = 1,000 and simulate n coin flips. 
Plot the proportion of heads as a function of n. 
Repeat for P = .03.

"""

import matplotlib.pyplot as plt
import random
import sys
import numpy as np

def weighted_coin_flip(p_heads):
    """
    weighted_coin_flip -> {0,1}
    1 = heads, with probability p_heads
    0 = tails, with probability 1 - p_heads
    """
    
    if random.random() < p_heads:
        return 1
    else:
        return 0

def main():
    
    n = 1000
    p1 = 0.3
    p2 = 0.03
    
    flips1 = np.array( [weighted_coin_flip(p1) for _ in range(n)] )
    flips2 = np.array( [weighted_coin_flip(p2) for _ in range(n)] )
    
    prop_heads1 = np.zeros(n) #proportion of flips that are heads
    prop_heads2 = np.zeros(n)
    
    for i in range(n):
        prop_heads1[i] = sum(flips1[:i+1])/(i+1)
        prop_heads2[i] = sum(flips2[:i+1])/(i+1)
        
    flip_count = np.arange(1,1001) #flip count
    
    plt.figure(1)
    plt.title('Proportion of heads for two weighted coins')
    plt.subplot(211)
    plt.plot(flip_count, prop_heads1)
    plt.xlabel('number of flips')
    plt.ylabel('prop. of heads (P = 0.3)')
    
    plt.subplot(212)
    plt.plot(flip_count, prop_heads2)
    plt.xlabel('number of flips')
    plt.ylabel('prop. of heads (P = 0.03)')
    
    plt.show()
    
if __name__ == '__main__':
    main()
    



