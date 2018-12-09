#!/usr/bin/env python3
import lib
N=10**8

result = set()
i = 1
while i < N**0.5:
  sm = i*i
  j = i+1
  sm += j**2 # must be at least two squares
  j += 1
  while sm < N:
    if lib.is_palindrome(sm):
      print(i,'..',j,sm)
      result.add(sm)
    sm += j**2
    j += 1
  i += 1

print(sum(result))