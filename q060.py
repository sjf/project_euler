#!/usr/bin/env py3
import lib
N= 100000
MX= 30000
sieve =lib.prime_sieve(N)
primes = lib.primes(MX)

def ok(a,b):
  x = lib.concat(a,b)
  if x < N:
    if not sieve[x]:
      return False
  elif not lib.is_prime(x):
    return False

  y = lib.concat(b,a)
  if y < N:
    if not sieve[y]:
      return False
  elif not lib.is_prime(y):
    return False
  return True

mn = N*5
mn_val = []
cnt = 0
mx = len(primes)
for i in range(mx):
  a = primes[i]

  for j in range(i+1, mx):
    b = primes[j]
    sm = a + b
    if sm > mn or not ok(a,b):
      continue

    for k in range(j+1, mx):
      c = primes[k]
      sm = a + b + c
      if sm > mn or not (ok(a,c) and ok(b,c)):
        continue

      for l in range(k+1,mx):
        d = primes[l]
        sm = a + b +c + d
        if sm > mn or not(ok(a,d) and ok(b,d) and ok(c,d)):
          continue

        for m in range(l+1,mx):
          e = primes[m]
          sm = a + b +c + d + e
          cnt += 1

          if cnt %100000 ==0: print(' ',a,b,c,d,' ',i,j,k,l)
          
          if sm > mn or not(ok(a,e) and ok(b,e) and ok(c,e) and ok(d,e)):
            continue

          print(sm,' ',a,b,c,d,e)
          if sm < mn:
            mn = sm
            mn_val = (a,b,c,d,e)

print(mn,mn_val)


      
