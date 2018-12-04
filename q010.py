#!/usr/bin/env python
from lib import primes
N=2_000_000
pr = primes(N)
print(sum(primes(N)))