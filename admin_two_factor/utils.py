import datetime
import time

from admin_two_factor import settings


def str_to_date(timestamp):
    """
    Convert seconds to date and time
    :param timestamp: This field should be in seconds
    :type timestamp: int field
    :return: date instance
    """
    date_time = datetime.datetime.fromtimestamp(timestamp)
    return date_time


def str_to_time(_date):
    """
    Convert date and time to seconds
    :param _date: This field should be in date
    :return: int
    """
    result = int(time.mktime(_date.timetuple()))
    return result


def set_expire(interval=settings.SESSION_COOKIE_AGE):
    """
    Convert date and time to the future
    :param interval: The interval should be to hour
    :return: array
    """
    _date = datetime.datetime.now()
    expire_time = (interval * 60 * 60) + str_to_time(_date)
    expire_date = str_to_date(expire_time)
    return dict(date=expire_date, time=expire_time)


def is_expired(ex_time, now=None):
    now = datetime.datetime.now() if not now else now
    if ex_time <= str_to_time(now):
        return True
    return False
