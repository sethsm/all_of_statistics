#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 16:15:32 2016

@author: sethstrimas-mackey

All of Stats, Q1.22 
Suppose we flip a coin n times and let P 
denote the probability of heads. Let X be the number of heads. 
We call X a binomial random variable, which is discussed in 
the next chapter. Intuition suggests that X will be close to n*p. 
To see if this is true, we can repeat this experiment many times 
and average the X values. Carry out a simulation and compare the
average of the X's to n p . Try this for p =.3 and n = 10, n = 100, 
and n = 1,000.

"""

import matplotlib.pyplot as plt
import random
import sys
import numpy as np

def weighted_coin_flip(p_heads):
    '''
    return:
    1 = heads, with probability p_heads
    0 = tails, with probability 1 - p_heads
    '''
    
    if random.random() < p_heads:
        return 1
    else:
        return 0
        
def avg_num_heads(p_heads, n_flips, n_trials=10000):
    '''
    av_num_heads -> avg number of heads in n_flips flips over n_trials trials.
    '''
    num_heads = 0
    
    for _ in range(n_trials*n_flips):
        num_heads += weighted_coin_flip(p_heads)
    
    return num_heads/n_trials
            
    
def main():
    
    p_heads = 0.3
    N = (10, 100, 1000)
    
    avg_heads  = [avg_num_heads(p_heads, n_flips) for n_flips in N]
    exp_heads = [n_flips*p_heads for n_flips in N]
    
    print('Flips | Avgerage | Expected')

    for i in range(len(avg_heads)):
        print(N[i], avg_heads[i], exp_heads[i])
        
if __name__ == '__main__':
    main()

