import pytz
import time
from datetime import datetime

UNIX_TIMESTAMP_UNIT = {
    'seconds': 1,
    'miliseconds': 1000,
    'microseconds': 1000000
}


class DatetimeConverter(object):

    def __init__(self, dt):
        if not dt.tzinfo:
            self._dt_utc = dt.replace(tzinfo=pytz.utc)
        else:
            self._dt_utc = dt.astimezone(pytz.utc)
        self._tz = dt.tzinfo

    def to_timestamp_seconds(self):
        return time.mktime(self._dt_utc.timetuple()) + self._dt_utc.microsecond / UNIX_TIMESTAMP_UNIT['microseconds']

    def to_timestamp_miliseconds(self):
        return self.to_timestamp_seconds() * UNIX_TIMESTAMP_UNIT['miliseconds']

    def to_timestamp_microseconds(self):
        return self.to_timestamp_seconds() * UNIX_TIMESTAMP_UNIT['microseconds']

    def to_datetime_utc(self):
        return self._dt_utc

    def to_datetime_with_timezone(timezone):
        pass


class TimestampConverter(DatetimeConverter):

    def __init__(self, timestamp, unit='miliseconds'):
        dt = datetime.utcfromtimestamp(float(timestamp) / UNIX_TIMESTAMP_UNIT[unit])
        super(TimestampConverter, self).__init__(dt)