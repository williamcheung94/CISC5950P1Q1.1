#!/usr/bin/python
from operator import itemgetter
import sys

dict_ip_count = {}

for line in sys.stdin:
    line = line.strip()
    time, num = line.split('\t')
    try:
        num = int(num)
        dict_ip_count[time] = dict_ip_count.get(time, 0) + num

    except ValueError:
        pass

sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(1), reverse=True)
for time, count in sorted_dict_ip_count:
    print '%s\t%s' % (time, count)
