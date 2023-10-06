#!/usr/bin/env python3

import sys, os

sys.path.append(os.path.abspath("pydate"))

from pydate import Year, Date, Time, DateTime

demo_year = Year()
demo_date = Date()
demo_time = Time()
demo_datetime = DateTime()

demo_year.set_year_UTC()
print (str(f"Demo Year: {demo_year.tostring()}"))

demo_date.set_year_UTC()
demo_date.set_month_UTC()
demo_date.set_day_UTC()
print (str(f"Demo Date: {demo_date.tostring()}"))

demo_time.set_hour_UTC()
demo_time.set_minute_UTC()
demo_time.set_second_UTC()
print (str(f"Demo Time: {demo_time.tostring()}"))

demo_datetime.set_UTC()
print (str(f"Demo DateTime: UTC - {demo_datetime.get_gregorian()} {demo_datetime.tostring()}"))

timezones = [
    'AST',
    'EDT',
    'EST',
    'CDT',
    'CST',
    'MDT',
    'MST',
    'PDT',
    'PST',
    'AKDT',
    'AKST',
    'HDT',
    'HST',
    'SST'
]

for timezone in timezones:
    demo_datetime.set_timezone(timezone)
    print (str(f"Demo DateTime: {timezone} - {demo_datetime.get_gregorian()} {demo_datetime.tostring()}"))