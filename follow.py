# follow.py
#
# watch a log file

import os
import time


def follow(filename):

    f = open(filename, 'r')
    f.seek(0, os.SEEK_END)

    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


for line in follow('/var/log/auth.log'):
    if 'opened' in line:
        info = line.split(':')[-1].split('by')
        print('Session opened for user: {} by {}'.format(
                info[0].split('user')[-1].strip(),
                info[1].strip()))

    print('Got:', line)
