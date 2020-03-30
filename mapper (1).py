#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys

pat = re.compile('(?P<hour>\d{4}[A|P])')
matched = {}
for line in sys.stdin:
    match = pat.search(line) 
    if match:
        time = match.group('hour')
        if ('A' in time):
            time = int(time[:2])
        elif ('P' in time):
            time = int(time[:2])+12
        else:
            time = int(time[:2])
        if time not in matched.keys():
            matched[time] = 1
        else:
            matched[time] += 1

for i in matched.items():
    print '%s\t%s' % (i[0], i[1])

