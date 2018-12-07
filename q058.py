#!/usr/bin/env python3
import lib
N=688590081
sieve = lib.get_prime_sieve(N)

def get_corners(n):
  return [n**2 - 3*(n-1),
          n**2 - 2*(n-1),
          n**2 - (n-1),
          n**2]

def get_candidate_corners(n):
  if n%3==0:
    c0 = 0
  else:
    c0 = n**2 - 3*(n-1)

  if (n+1)%5 == 0 or (n+2)%5 == 0:
    c1 = 0
  else:
    c1 = n**2 - 2*(n-1)

  if (n+1)%3 == 0:
    c2 = 0
  else:
    c2 = n**2 - (n-1)

  corners = (c0,c1,c2)
  return corners

prime_cnt = 0
i = 3
while i < N:
  # cs1 = get_corners(i)
  # cs = get_candidate_corners(i)
  # out = []
  # rest = []
  # for j in range(len(cs)):
  #   c = cs[j]
  #   if c and not lib.is_prime(c):
  #     out.append("*" + str(c))
  #     if j == 2:
  #        f = lib.get_factors(c)
  #        f.remove(1)
  #        f.remove(c)
  #        f.sort()
  #        f = map(str,f)
  #        rest.append(str(c)+':'+",".join(f))
  #   else:
  #     out.append(str(c))
  #   #rest = [str(cs1)]
  # print(str(i)+':',", ".join(out),' ',"; ".join(rest))
  # i+=2
  cs=get_candidate_corners(i)
  #print(i,cs)
  for c in cs:
    if c != 0 and (c < len(sieve) and sieve[c]) or lib.is_prime(c):
    #if c != 0 and lib.is_prime(c):
      prime_cnt += 1
    # else:
    #   print(i,c)
  n_corners = ((i//2)*4)+1
  ratio = prime_cnt/n_corners
  print(i,prime_cnt,n_corners, ratio)
  if ratio < 0.1:
     print(i,ratio)
     break
  i += 2

