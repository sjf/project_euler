#!/usr/bin/env python3
import lib

prime_cnt = 0
corner_cnt = 1
side = 3
i = 1
N=999999999
ratio = 1
while i < N:
  for j in range(3):
    i += side-1
    if lib.is_prime(i):
      prime_cnt += 1
  #fourth corner is never prime
  i += side-1
  corner_cnt += 4

  ratio = prime_cnt/corner_cnt
  if side % 1001 == 0: print(side,prime_cnt,corner_cnt, ratio)
  if ratio < 0.1:
    print(side,ratio)
    break
  
  side += 2
  
