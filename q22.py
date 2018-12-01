#!/usr/bin/env python3

txt = open('p022_names.txt').read()
txt.strip()
names = list(map(lambda s: s.strip('"'), txt.split(",")))
names.sort()
sums = list(map(lambda s: sum(map(lambda c: ord(c) - ord('A') + 1, s)), names))
print(sum([(i+1) * sums[i] for i in range(len(sums))]))