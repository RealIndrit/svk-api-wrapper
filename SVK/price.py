import json
from SVK.svk import SVK
from SVK.constants import PRICE
from SVK.types.unix_milli_seconds import UnixMillisecondSecond


class PriceHelper(SVK):
    def get_data(self, unix: UnixMillisecondSecond) -> json:
        return self._get_data(PRICE, unix)
