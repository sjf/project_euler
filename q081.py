#!/usr/bin/env python3
import lib

M=[[131,673,234,103, 18],
   [201, 96,342,965,150],
   [630,803,746,422,111],
   [537,699,497,121,956],
   [805,732,524, 37,331]]

M = lib.read_nums_from_file('p081_matrix.txt')
N=len(M)

for i in range(1,N):
  # edges have only one possible path
  M[0][i] += M[0][i-1]
  M[i][0] += M[i-1][0]

for i in range(1,N):
  for j in range(1,N):
    # choose previous step in path with minimum value
    M[i][j] += min(M[i-1][j],M[i][j-1])

print(M[N-1][N-1])

