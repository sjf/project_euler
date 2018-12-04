#!/usr/bin/env python3
from math import log
from lib import primes
N=10_001
lim = int(N * log(N) + 3)*2 #from Prime Number Theorum

pr = primes(lim+1)
print(pr[N-1])
