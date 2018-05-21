# coding: utf-8

'learn from https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431937554888869fb52b812243dda6103214cd61d0c2000'

__author__ = 'banyaofei'

from datetime import datetime, timezone, timedelta
import re

def to_timestamp(dt_str, tz_str):
    utc = int(re.match(r'^UTC([+|-][0-9]+):([0-9])+', tz_str).group(1))
    local_time = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')

    utc_zone = timezone(timedelta(hours=utc))
    local_time = local_time.replace(tzinfo=utc_zone)

    return local_time.timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
