#!/usr/bin/env python3
N=3

def positive_bits(i):
  res = 0
  while i:
    if i & 1:
      res += 1
    i = i >> 1
  return res

max = 2**(N*2)
i = 0
count = 0
while i < max:
  if positive_bits(i) == N:
    count += 1
  i += 1
  print (i,count)

print(count)

