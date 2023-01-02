import json
from SVK.svk import SVK
from SVK.constants import *


class ProductionHelper(SVK):
    def get_data(self, date, country_code) -> json:
        return self._get_data(PRODUCTION, date, country_code)
