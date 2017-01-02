import logging
import os
import time
import datetime

import sys

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


def get_logger(name):
    py_path = os.path.split(os.path.realpath(sys.argv[0]))[0]
    LOG_FILE = os.path.join(py_path, name + "logger.log")
    handler = logging.FileHandler(LOG_FILE, mode='a')
    fmt = "%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s"
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger



