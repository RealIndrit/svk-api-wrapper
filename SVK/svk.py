import json
import requests
from SVK.constants import API


class SVK():
    def __init__(self):
        # -1 = unintilized, data has been never retreived for this endpoint in this run instance
        self.updated_time: int = -1

    def _get_data(self, api_end: str, *param) -> json:
        url = API + api_end.format(*param)
        json_data = json.loads(requests.get(url).content)
        self.updated_time = json_data["LastUpdated"]
        return json_data
