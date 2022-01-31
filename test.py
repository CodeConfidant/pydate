#!/usr/bin/env python3

import sys, os

sys.path.append(os.path.abspath("pydate"))

from pydate import Year, Date, Time, DateTime

demo_year = Year()
demo_date = Date()
demo_time = Time()
demo_datetime = DateTime()

demo_year.set_year_UTC()
print("Demo Year: ", demo_year.tostring())

demo_date.set_year_UTC()
demo_date.set_month_UTC()
demo_date.set_day_UTC()
print("Demo Date: ", demo_date.tostring())

demo_time.set_hour_UTC()
demo_time.set_minute_UTC()
demo_time.set_second_UTC()
print("Demo Time: ", demo_time.tostring())

demo_datetime.set_UTC()
print("Demo DateTime: UTC -", demo_datetime.get_gregorian(), demo_datetime.tostring())

demo_datetime.set_EST()
print("Demo DateTime: EST -", demo_datetime.get_gregorian(), demo_datetime.tostring())

demo_datetime.set_EDT()
print("Demo DateTime: EDT -", demo_datetime.get_gregorian(), demo_datetime.tostring())