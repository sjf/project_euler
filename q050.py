#!/usr/bin/env python3
import lib
N=1_000_000
sieve = lib.get_prime_sieve(N)
primes = lib.primes(N,sieve)

mx = 0
mx_sum = None
for i in range(len(primes)):
  sum = primes[i]
  for j in range(i+1,len(primes)):
    sum += primes[j]
    if sum >= N:
      break
    if sieve[sum]:
      if j-i > mx:
        mx = j-i
        mx_sum=sum
print(mx+1,mx_sum)
