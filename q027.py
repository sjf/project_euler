#!/usr/bin/env python3
import lib
A=1000
B=1001

def quad(a,b,n):
  return (n*n) + (a*n) + b

prime = lib.get_prime_sieve(100_000)
# B must be prime
b_list = []
for i in range(B):
  if prime[i]:
    b_list.append(i)
    b_list.append(-i)

max_cnt = 0
max_prod = 0
# A must be even for a+b+1 to odd, all primes >2 are odd
for a in range(-A+1,A,2):
  for b in b_list:
    if abs(b) == 2:
       a -= 1
    i = 0
    while prime[quad(a,b,i)]:
      i += 1
    #print(a,b,i)
    if i >= max_cnt:
      max_prod = a*b
      max_cnt = i
print(max_prod)
