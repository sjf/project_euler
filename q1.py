#!/usr/bin/env python
N=1000
sum=0
for i in range(1, N):
	if i % 5 == 0 or i % 3 == 0:
		sum += i
print sum