#!/usr/bin/env python3
N=20

counts = [[0 for i in range(N+1)] for j in range(N+1)]

pts = [(N,N)]

for i in range(N+1):
  #initialize top and left edges, they have one only path
  counts[0][i] = 1
  counts[i][0] = 1

#other points have the sum of the points up & left
for i in range(1, N+1):
  for j in range(1, N+1):
    counts[i][j] = counts[i-1][j] + counts[i][j-1]
      
print(counts[N][N])
