#!/usr/bin/env python3
import lib
from math import sqrt
mn = 1010101030
#mn= (int(sqrt(1020304050607080900))//10)*10
mx=int(sqrt(1929394959697989990))

def check(n):
  for i in range(1,10):
    if lib.get_digit(n, (9-i+1)*2) != i:
      return False
  return True

x = 0
mmx= 0
i = mn
inc = 40
while i <= mx:
  if i %10000000 == 30:print((i-mn)/(mx-mn))
  n = i*i
  #print(n)
  ok = check(n)
  if ok:
    print(i,n)
    break
  # squares that end in 0 have roots that end in 0    
  # squares that end 9 have roots that end in 3 or 7
  i += inc
  inc = 40 if inc == 60 else 60



