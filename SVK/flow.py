import json
from SVK.svk import SVK
from SVK.constants import *


class FlowHelper(SVK):
    def get_data(self, unix) -> json:
        return self._get_data(FLOW, unix)
