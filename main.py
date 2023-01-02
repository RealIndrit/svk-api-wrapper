import datetime
from SVK.flow import FlowHelper
from SVK.frequency import FrequencyHelper
from SVK.price import PriceHelper
from SVK.production import ProductionHelper
from SVK.situation import SituationHelper


def main():
    pass


if __name__ == "__main__":
    frh = FrequencyHelper()
    print(frh.get_data(1672650000000, 1672679282548))
    print(frh.updated_time)
    print(int(datetime.datetime.utcnow().timestamp() * 1000))
