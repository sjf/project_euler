#!/usr/bin/env python3
import lib
N=5

def output(vals):
  mn = min(vals[N:])
  while vals[N] != mn:
    # rotate
    nxt = [0] * len(vals)
    for i in range(len(vals)):
      val = vals[i]
      if i < N:
        j = (i + 1) % N
      else:
        j = ((i + 1 - N) % N) + N
      nxt[j] = val
    vals = nxt
  out = []
  for i in range(N):
    out.extend([vals[N+i], vals[i], vals[(i + 1) % N]])
  return int("".join(map(str,out)))

def check(vals):
  ten = vals.index(10)
  # 10 must appear on the outside to produce a result 
  # with 16 digits
  if ten < N: 
    return (0,0)
  target = vals[N] + vals[0] + vals[1]
  for i in range(1,N):
    line = vals[N+i] + vals[i] + vals[(i + 1) % N]
    if line != target:
      return (0,0)
  return (target, output(vals))

mx=0
vals = list(range(1,(N*2)+1))
for perm in lib.permutations_lexico(vals):
  sm,res = check(perm)
  if res:
    if len(str(res)) == 16:
      print(sm, res, '('+str(len(str(res)))+')')
      mx = max(mx, res)

print('result', mx)
