#!/usr/bin/env python3
from lib import first, second, push
from collections import Counter
import sys

F='p054_poker.txt'

J = 11
Q = 12
K = 13
A = 14

def parse_card(s):
  print(s)
  v = s[0]
  val = 0
  if v in '23456789':
    val = int(s[0])
  elif v == 'T':
    val = 10
  elif v == 'J':
    val = J
  elif v == 'Q':
    val = Q
  elif v == 'K':
    val = K
  elif v == 'A':
    val = A
  d = s[1]
  return (val, d)

def is_consecutive(l):
  for i in range(1, len(l)):
    if l[i] != l[i-1] + 1:
      return False
  return True

def same_val(l, n):
  cnt = Counter(l)
  for val in cnt.keys():
    if cnt[val] == n:
      return val
  return 0

def parse_hand(s):
  s = s.strip()
  cards = list(map(parse_card, s.split(' ')))
  h1 = cards[:5]
  h2 = cards[5:]
  return (h1, h2)
  
def score(hand):
  vals = list(map(first, hand))
  vals.sort()
  suits = list(map(second, hand))
  same_suit = len(set(suits)) == 1

  score = vals[:]
  score.reverse()

  if vals == [10, J, Q, K, A] and same_suit:
    #royal flush
    push(score, 0)
    push(score, 23)
    return score
  if is_consecutive(vals) and same_suit:
    #straight flush
    push(score, 0)
    push(score, 22)
    return score
  four = same_val(vals, 4)
  if four:
    #4 of a kind
    push(score,four)
    push(score,21)
    return score
  three = same_val(vals, 3)
  two = same_val(vals, 2)
  if three and two:
    #full house
    push(score,three)
    push(score,20)
    return score
  if same_suit:
    #flush
    push(score, 0)
    push(score,19)
    return score
  if is_consecutive(vals):
    #straight
    push(score, 0)
    push(score,18)
    return score
  if three:
    #3 of a kind
    push(score,three)
    push(score,17)
    return score
  pair1 = same_val(vals[0:3], 2)
  pair2 = same_val(vals[2:], 2)
  if pair1 and pair2:
    #2 pairs
    push(score,max(pair1,pair2))
    push(score,16)
    return score
  if two:
    #one pair
    push(score,two)
    push(score,15)
    return score
  # high card
  push(score, max(vals))
  return score

txt = open(F).read()
lines = txt.strip().split('\n')
hands = list(map(parse_hand, lines))

count = 0
for hand in hands:
  print(hand)
  p1,p2 = hand
  s1 = score(p1)
  s2 = score(p2)
  print(s1,s2)
  if s1 > s2:
    print('*')
    count += 1

print(count)