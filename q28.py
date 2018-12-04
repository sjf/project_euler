#!/usr/bin/env python3
N=1001

def sq(n):
  return 4*(n**2) - (6*n) +6

sum = 1
for i in range(3,N+1,2):
  print (i, sq(i))
  sum += sq(i)
print(sum)
