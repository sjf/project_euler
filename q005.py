#!/usr/bin/env python3
import lib
from collections import Counter

# The prime factors of each number 1 to 20
counts = ([Counter(lib.prime_factors(i)) for i in range(2,21)])
total = Counter()
# Get the max count of each factor
for count in counts:
  for n in count:
    if total[n] < count[n]:
      total[n] = count[n]

res = lib.multiply([n ** total[n] for n in total.keys()])
print(res)