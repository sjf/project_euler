#!/usr/bin/env python3
import lib
n=1
d=1
i=0
N=1000
count = 0
while i < N+1:
  #print(i,str(n)+'/'+str(d),n/d)
  if (lib.num_digits(n) >lib.num_digits(d)):
    count += 1
  #term' = 1 + 1/(1+term)
  n+= d #1 + term
  n,d=d,n #1/(1+term)
  n+= d #1+1/(1+term)
  
  i+=1
print(count)

