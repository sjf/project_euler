#!/usr/bin/env python3
import lib

N=100
dp=[[0]*(N+1) for i in range(N-1)]
for i in range(N-1):
  dp[i][0] = 1 # one way to make 0 using (i+1)
for j in range(N+1):
  dp[0][j] = 1

for i in range(1,N-1):
  num = i + 1
  for total in range(1,N+1):
    dp[i][total] = dp[i-1][total] #can use values less than num
    if num == total:
      dp[i][total] += 1 # one way to make total using num, plus ways using numbers < num
    elif num < total:
      diff = total-num
      dp[i][total] += dp[i][diff] # add ways to make total-num using numbers <= num


print(dp[98][100])

