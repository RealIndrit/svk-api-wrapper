import datetime
import time
from SVK.flow import FlowHelper
from SVK.frequency import FrequencyHelper
from SVK.price import PriceHelper
from SVK.production import ProductionHelper
from SVK.situation import SituationHelper
from SVK.types.date_day import DateDay
from SVK.types.unix_milli_seconds import UnixMillisecondSecond


def main():
    pass


if __name__ == "__main__":
    date_time = DateDay(time.gmtime())
    date_date_time = DateDay(datetime.datetime.utcnow())
    unix_milli_sec_time = UnixMillisecondSecond(time.gmtime())
    unix_milli_sec_datetime = UnixMillisecondSecond(datetime.datetime.utcnow())
    print(date_time, date_date_time)
    print(unix_milli_sec_time, unix_milli_sec_datetime)

    h = ProductionHelper()
    data = h.get_data(date_time, "TO")
    print(data)
