import json
from SVK.svk import SVK
from SVK.constants import *


class FrequncyHelper(SVK):
    def get_data(self, lower_unix, upper_unix) -> json:
        return self._get_data(FREQ, lower_unix, upper_unix)
