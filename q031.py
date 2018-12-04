#!/usr/bin/env python3
from collections import defaultdict
import lib
COINS=[1,2,5,10,20,50,100,200]
N=200

_dp = []

def f(total):
  for i in range(len(COINS)):
    _dp.append([0] * (total+1))

  for i in range(len(COINS)):
    _dp[i][0] = 1 # 1 way to zero p
  for i in range(total+1):
    _dp[0][i] = 1 # 1 way to make n using 1p coin

  for i in range(1,total+1):
    for c in range(1,len(COINS)):
      # can make i using the coins less than c
      _dp[c][i] = _dp[c-1][i]
      if i == COINS[c]:
        # can make i using one c coin
        _dp[c][i] += 1
      if i - COINS[c] > 0:
        # can make i using c and the other coins
        _dp[c][i] += _dp[c][i-COINS[c]]
f(N)
print(_dp[len(COINS)-1][N])