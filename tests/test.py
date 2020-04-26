#!/usr/bin/env python3

import sys, os

sys.path.append(os.path.abspath("../pydate-date/pydate"))

from pydate import Year, Date, Time, DateTime

demo_year = Year(2020)
demo_date = Date(2020, 4, 26)
demo_time = Time(14, 27, 37)
demo_datetime = DateTime(2020, 4, 26, 14, 27, 37)

print(demo_year.tostring())
print(demo_date.tostring())
print(demo_time.tostring())
print(demo_datetime.tostring())

del(demo_year, demo_date, demo_time, demo_datetime)