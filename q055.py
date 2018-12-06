#!/usr/bin/env python3
import lib
N=10000
cnt = 0

def is_lychrel(n):
  i = 1
  while i < 50:
    nx = n + lib.reverse(n)
    if lib.is_palindrome(nx):
      return False
    n = nx
    i += 1
  return True 

for i in range(1,N):
  if is_lychrel(i):
    cnt += 1
print(cnt)
        

