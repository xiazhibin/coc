import time
import datetime

UTC_FORMAT = '%Y%m%dT%H%M%S.%fZ'


def utc2local(utc_st):
    now_stamp = time.time()
    local_time = datetime.datetime.fromtimestamp(now_stamp)
    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st


def convert_utc_time(time_str):
    time_str = time_str.encode('ascii')
    return utc2local(datetime.datetime.strptime(time_str, UTC_FORMAT))


def datetime_to_timestamp(date_time):
    if date_time:
        return time.mktime(date_time.timetuple())
    else:
        return None
