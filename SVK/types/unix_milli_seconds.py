from datetime import datetime
import time
from typing import Union


class UnixMillisecondSecond(object):
    def __init__(self, timestamp: Union[int, float, str, datetime, time.struct_time]):

        if isinstance(timestamp, datetime):
            timestamp = timestamp.timestamp() * 1000
        elif isinstance(timestamp, time.struct_time):
            timestamp = time.mktime(timestamp) * 1000
        else:
            try:
                timestamp = int(timestamp)
            except:
                raise ValueError(
                    f"{timestamp} cannot be converted to a int value!")

        if timestamp < 0:
            raise ValueError(f"{timestamp} cannot be negative")
        # Make value to int to cut off all excessive float number and then convert to string to round to closest full second
        unix_string = str(int(timestamp))
        if len(unix_string) <= 3:
            raise ValueError(
                f"{timestamp} has to be a full second of milliseconds")

        # Replace the last 3 digits with 0 toi make it even seconds value
        unix_string = unix_string.replace(
            unix_string[len(unix_string) - 3:], "000")

        self._timestamp = int(unix_string)

    def __repr__(self) -> str:
        return '{0}'.format(self._timestamp)

    def __str__(self) -> str:
        return '{0}'.format(self._timestamp)

    def __add__(self, value):
        return UnixMillisecondSecond(self._timestamp + value)

    def __sub__(self, value):
        return UnixMillisecondSecond(self._timestamp - value)

    @property
    def real(self) -> int:
        return self._timestamp
