#!/usr/bin/env python3
import lib
mul=28433
pw=7830457
tendigits = 10**10

n=1
for i in range(1,pw+1):
  n *= 2
  n = n%(tendigits)
n *= mul
n += 1
n = n%(tendigits)
print(n)

