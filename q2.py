#!/usr/bin/env python3
N=4_000_000
f1 = 1
f2 = 2
sum = 0
while f2 < N:
	if f2 % 2 == 0:
		sum += f2
	f = f1 + f2
	f1,f2 = f2,f
print(sum)