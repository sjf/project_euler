#!/usr/bin/env python
N=1000
named = {1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        10:'ten',
        11:'eleven',
        12:'twelve',
        13:'thirteen',
        14:'fourteen',
        15:'fifteen',
        16:'sixteen',
        17:'seventeen',
        18:'eighteen',
        19:'nineteen',
        20:'twenty',
        30:'thirty',
        40:'forty',
        50:'fifty',
        60:'sixty',
        70:'seventy',
        80:'eighty',
        90:'ninety',
        1000:'onethousand'
}
H=len('hundred')
A=len('and')
_memo = {}
for n in named:
  _memo[n] = len(named[n])

def name(n):
  if n in _memo:
    return _memo[n]

  h = int(n / 100)
  if h:
    ln = _memo[h] + H # N hundred
    rest = n%100
    if rest:
      ln += A + _memo[rest] # and DD
    _memo[n] = ln
    return ln
  d = int(n / 10) * 10
  ln = _memo[d] + _memo[n % d] #Nty N
  _memo[n] = ln
  return ln

result = 0
for i in range(1,N+1):
  result += name(i)
print(result)