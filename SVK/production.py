import json
from SVK.svk import SVK
from SVK.constants import PRODUCTION
from SVK.types.date_day import DateDay


class ProductionHelper(SVK):
    def get_data(self, date: DateDay, country_code) -> json:
        return self._get_data(PRODUCTION, date, country_code)
