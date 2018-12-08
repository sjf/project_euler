#!/usr/bin/env python3
import lib
from math import log

pairs = lib.read_nums_from_file('p099_base_exp.txt')
mx = 0
mx_i = 0
# log(a^b) = b*log(a)
for i in range(len(pairs)):
  a,b = pairs[i]
  print(i,a,b)
  val = b*log(a)
  print(i,a,b,val)
  if val > mx:
    mx = val
    mx_i = i+1
print(mx,mx_i)

