#!/usr/bin/env python3

import sys, os

sys.path.append(os.path.abspath("pydate"))

from pydate import Year, Date, Time, DateTime


demo_datetime = DateTime(2020, 1, 1, 1, 1, 1)

demo_datetime.set_UTC()
print("UTC -", demo_datetime.get_gregorian(), demo_datetime.tostring())

demo_datetime.set_EST()
print("EST -", demo_datetime.get_gregorian(), demo_datetime.tostring())
