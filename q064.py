#!/usr/bin/env python3
import lib
N=10_000

count = 0
for i in range(1,N+1):
  fraction = lib.sqrt_continued_fraction(i)
  print(i, fraction)
  if len(fraction[1:]) %2 == 1:
    count += 1

print(count)