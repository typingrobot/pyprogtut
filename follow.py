# follow.py
#
# watch a log file

import os
import time
import csv


def follow(filename):

    f = open(filename, 'r')
    f.seek(0, os.SEEK_END)

    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def parse_auth_log(lines):
    rows = csv.reader(lines)
    types = [str]
    converted = ([func(val) for func, val in zip(types, row)] for row in rows)
    return converted


lines = follow('/var/log/auth.log')
rows = parse_auth_log(lines)


for row in rows:
    if 'opened' in row[0]:
        info = row[0].split(':')[-1].split('by')
        print('Session opened for user: {} by {}'.format(
                info[0].split('user')[-1].strip(),
                info[1].strip()))
