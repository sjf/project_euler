#!/usr/bin/env python3
import lib
N=1_000_000
F=8
S=65003

sieve = lib.get_prime_sieve(N)
print('...')

def has_dups(n):
  cnt = {}
  for d in lib.to_digits(n):
    if d in cnt:
      cnt[d] += 1
    else:
      cnt[d] = 1
  return (0 in cnt and cnt[0] == 3) or \
         (1 in cnt and cnt[1] == 3) or \
         (2 in cnt and cnt[2] == 3)

for p in range(S,N,2):
  if not sieve[p]: continue
  if not has_dups(p): continue

  ln = lib.num_digits(p)
  for i in range(ln-1):
    for j in range(i+1,ln):
      for k in range(j+1,ln):
        terms = []
        d=0
        while d < 10:
          t = lib.set_digit(p,i,d)
          t = lib.set_digit(t,j,d)
          t = lib.set_digit(t,k,d)
          if sieve[t] and t >=p:
            terms.append(t)
          if 9-d < F-len(terms):
            break
          d += 1
        if len(terms) >= F:
          print(p,i,j,terms)
          break

        

