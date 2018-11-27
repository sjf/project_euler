#!/usr/bin/env python3
from math import sqrt
N=600851475143
p=2
while N >= p**2:
	if N % p == 0:
		#print(p)
		N /= p
	else:
		p += 1
print(int(N))
