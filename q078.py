#!/usr/bin/env python3
import lib

N=1_000_000
MX=1000

def partition2(n):
  """ Coin partitions. Let partition(n) represent the number of different ways in which n coins can be separated into piles. 
  For example, five coins can be separated into piles in exactly seven different ways, so partition(5)=7. """

  # dynamic programming table, table cell (i,j), parition size = i + 1, target n = i + 1, cell value = partition(n)
  dp = {} # using dict as dynamic programming table is really slow
  for i in range(n):
    dp[(0,i)] = 1 # One way to partition any n using piles of size 1
    dp[(i,0)] = 1 # One way to partition n=1

  for i in range(1,n):
    for j in range(1,n): 
      value = dp[(i-1,j)] # Include ways to partition n using piles <i
      if i == j:
        value += 1 # One way to make n using piles of the same size
      elif j > i:
        value += dp[(i,j-i-1)] # Include ways to make j-i using piles of size <i
      dp[(i,j)] = value

      if i == j:
        print(i+1,value)
        if value % N == 0:
          print('result',i+1,value)
          return value
  return dp[(n-1,n-1)]


def partition1(n):
  """ Coin partitions. Let partition(n) represent the number of different ways in which n coins can be separated into piles. 
  For example, five coins can be separated into piles in exactly seven different ways, so partition(5)=7. """

  # dynamic programming table, table cell (i,j), parition size = i + 1, target n = i + 1, cell value = partition(n)
  dp = [[0]*n for i in range(n)]
  for i in range(n):
    dp[0][i] = 1 # One way to partition any n using piles of size 1
    dp[i][0] = 1 # One way to partition n=1

  for i in range(1,n):
    for j in range(1,n): 
      value = dp[i-1][j] # Include ways to partition n using piles <i
      if i == j:
        value += 1 # One way to make n using piles of the same size
      elif j > i:
        value += dp[i][j-i-1] # Include ways to make j-i using piles of size <i
      dp[i][j] = value % N

      if i == j:
        if i%100 == 0: print(i+1,value)
        if value % N == 0:
          print('result',i+1,value)
          return value
  return dp[n-1][n-1]

def partition3(n):
  """ Coin partitions. Let partition(n) represent the number of different ways in which n coins can be separated into piles. 
  For example, five coins can be separated into piles in exactly seven different ways, so partition(5)=7. """

  # dynamic programming table
  # p(n) = p(n - gpenta(1)) + p(n - gpenta(2)) - p(n - gepenta(3)) - p(n - gpenta(4)) ...
  dp = [0]*(n+1)
  dp[0] = 1
  for i in range(1,n+1):
    penta = 1
    value = 0
    k = 0
    while i-lib.gpentagonal(penta) >= 0:
      sign = 1 if k < 2 else -1
      value += sign * dp[i-lib.gpentagonal(penta)]
      penta += 1
      k = (k + 1) % 4
    dp[i] = value % N
    if dp[i] % N == 0:      
      print(' solution',i,dp[i])
      return dp[i]
  return dp[n]


for i in range(1,10):
  if partition1(i) != partition3(i):
    print (i,partition3(i),'should be',partition1(i))
#lib.print2d(partition(5),rows=range(1,6),cols=range(1,6))
print(partition3(100000))
