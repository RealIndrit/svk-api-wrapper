import json
from SVK.svk import SVK
from SVK.constants import *


class SituationHelper(SVK):
    def get_data(self, date, bidding_area) -> json:
        return self._get_data(SITUATION, date, bidding_area)
