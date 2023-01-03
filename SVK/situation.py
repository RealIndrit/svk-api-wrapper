import json
from SVK.svk import SVK
from SVK.constants import SITUATION
from SVK.types.date_day import DateDay


class SituationHelper(SVK):
    def get_data(self, date: DateDay, bidding_area) -> json:
        return self._get_data(SITUATION, date, bidding_area)
