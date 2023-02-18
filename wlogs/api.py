import json
from pathlib import Path
from dataclasses import dataclass

import requests

# https://www.warcraftlogs.com/api/docs
TOKEN_URL = "https://www.warcraftlogs.com/oauth/token"
AUTH_FLOW_DATA = {'grant_type': 'client_credentials'}


@dataclass
class Client:
    _client_id: str
    _client_secret: str
    _authorize_url: str
    _token_url = TOKEN_URL
    _auth_flow_data = AUTH_FLOW_DATA
    _access_token: str = ""

    def __post_init__(self):
        response = requests.post(url=self._token_url,
                                 data=self._auth_flow_data,
                                 auth=(self._client_id, self._client_secret))
        self._access_token = response.json()['access_token']

    @property
    def authorize_url(self):
        return self._authorize_url

    @property
    def access_token(self):
        return self._access_token


def client_from_json(path: Path) -> Client:
    with open(path, 'r') as f:
        return Client(**json.load(f))


class Connector:
    def __init__(self, client: Client):
        self._post_url = client.authorize_url
        self._token = client.access_token
        self._headers = {'Authorization': 'Bearer ' + self._token}

    def post(self, query: str) -> dict:
        response = requests.get(self._post_url,
                                headers=self._headers,
                                json={'query': query})
        return json.loads(response.text)
