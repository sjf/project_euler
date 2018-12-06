#!/usr/bin/env python3
import lib
MOD=10**10

def pow(a,b):
  result = 1
  for i in range(b):
    result *= a
    result %= MOD
  return result

result = 0
for i in range(1,1000):
  result += pow(i,i)
  result %= MOD
print(result)