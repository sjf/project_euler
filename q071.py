#!/usr/bin/env python3
import lib, math
N=1_000_001

mn_val = (1,1)
mn_diff = (1,1)
for d in range(2,N+1):
  closest = None
  for n in range(int(d*(3/7)),N):
    a,b = lib.sub_fractions(3,7,n,d)
    if a <= 0:
      break
    closest = ((n,d),(a,b))
  if closest:
    val = closest[0]
    diff = closest[1]
    #print(mn_diff,diff)
    a,b = lib.sub_fractions(mn_diff[0],mn_diff[1],diff[0],diff[1])
    if a >= 0:
      mn_val = val
      mn_diff = diff
      #print('new min:',mn_val)
print(mn_val)
  



