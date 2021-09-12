#!/usr/bin/python3
# month/day/year
from datetime import date, timedelta
sdate = date(1900,1,1)
edate = date(2022,1,1)
delta = edate -sdate

for i in range(delta.days + 1):
  day = sdate + timedelta(days=i)
  #print(day.month,day.day,day.year)
  print(''.join([str(day.year), str(day.month), str(day.day)]))
