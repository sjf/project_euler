#!/usr/bin/env python3
_days=[0, 31, 28, 31,
      30, 31, 30,
      31, 31, 30,
      31, 30, 31]

def days(mon, year):
  if mon != 2:
    return _days[mon]
  if year % 4 == 0:
    if year % 100 or year % 400 == 0:
      return 29 # not a century or century divisible by 400
    return 28

def inc(day):
  year,mon,d,dow = day
  d += 1
  if d > days(mon, year):
    d = 1
    mon += 1
    if mon > 12:
      mon = 1
      year += 1
  dow += 1
  dow %= 7
  return (year,mon,d,dow)

day=(1900, 1, 1, 2) #year,mon,day,day of week(1 = sun)
while day[:3] < (1901,1,1):
  day = inc(day)

count = 0
while day[:3] < (2001,1,1):
  year,mon,d,dow = day
  if d == 1 and dow == 1:
    count += 1
  day = inc(day)
print(count)