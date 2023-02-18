import json
from pathlib import Path
from dataclasses import dataclass

import requests

# https://www.warcraftlogs.com/api/docs
TOKEN_URL = "https://www.warcraftlogs.com/oauth/token"
AUTH_FLOW_DATA = {'grant_type': 'client_credentials'}


@dataclass
class Client:
    client_id: str
    client_secret: str
    authorize_url: str
    token_url = TOKEN_URL
    auth_flow_data = AUTH_FLOW_DATA
    access_token: str = ""

    def __post_init__(self):
        response = requests.post(url=self.token_url,
                                 data=self.auth_flow_data,
                                 auth=(self.client_id, self.client_secret))
        self.access_token = response.json()['access_token']


def client_from_json(path: Path) -> Client:
    with open(path, 'r') as f:
        return Client(**json.load(f))
