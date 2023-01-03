import json
from SVK.svk import SVK
from SVK.constants import FREQ
from SVK.types.unix_milli_seconds import UnixMillisecondSecond


class FrequencyHelper(SVK):
    def get_data(self, lower_unix: UnixMillisecondSecond, upper_unix: UnixMillisecondSecond) -> json:
        return self._get_data(FREQ, lower_unix, upper_unix)
