#!/usr/bin/env python3
import lib
N=10000

penta={}
# def pentagon(n):
#   return int(n*(3*n-1)/2)
for n in range(1,N):
  penta[int(n*(3*n-1)/2)] = True
ps = list(penta.keys())
ps.sort()
for i in range(len(ps)):
  for j in range(i, len(ps)):
    a,b = ps[i],ps[j]
    if a + b in penta and b - a in penta:
      print(b-a)