import json
from SVK.svk import SVK
from SVK.constants import PRICE


class PriceHelper(SVK):
    def get_data(self, unix) -> json:
        return self._get_data(PRICE, unix)
