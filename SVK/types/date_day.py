from datetime import datetime
import time
from typing import Union


class DateDay(object):
    def __init__(self, datestamp: Union[datetime, time.struct_time, float]):
        if isinstance(datestamp, datetime):
            self._datestamp = datestamp.strftime('%Y-%m-%d')
        elif isinstance(datestamp, time.struct_time):
            self._datestamp = time.strftime('%Y-%m-%d', datestamp)
        elif isinstance(datestamp, float):
            self._datestamp = datetime.utcfromtimestamp(
                datestamp).strftime('%Y-%m-%d')
        else:
            raise ValueError(
                f"{datestamp} has to be type of datetime or struct_time (time) or a float unix timestamp value")

    def __repr__(self) -> str:
        return '{0}'.format(self._datestamp)

    def __str__(self) -> str:
        return '{0}'.format(self._datestamp)
