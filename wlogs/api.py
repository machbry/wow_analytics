import json
from pathlib import Path
from dataclasses import dataclass
from typing import Any

import requests

from .logger import Logger
from .conf import ROOT_DIRECTORY

logger = Logger().get()

# https://www.warcraftlogs.com/api/docs
TOKEN_URL = "https://www.warcraftlogs.com/oauth/token"
AUTH_FLOW_DATA = {'grant_type': 'client_credentials'}
CLIENT_CREDENTIALS_PATH = ROOT_DIRECTORY / "client_credentials.json"


@dataclass
class GraphQLClient:
    _client_id: str
    _client_secret: str
    _authorize_url: str
    _token_url = TOKEN_URL
    _auth_flow_data = AUTH_FLOW_DATA
    _access_token: str = ""

    def __post_init__(self):
        logger.debug(f"Token request for client {self._client_id} at {self._token_url}.")
        response = requests.post(url=self._token_url,
                                 data=self._auth_flow_data,
                                 auth=(self._client_id, self._client_secret))
        try:
            self._access_token = response.json()['access_token']
        except KeyError:
            logger.exception("Access token not retrieved.")
            raise
        else:
            logger.info("Access token retrieved.")
        self._headers = {'Authorization': 'Bearer ' + self._access_token}

    @property
    def authorize_url(self) -> str:
        return self._authorize_url

    @property
    def access_token(self) -> str:
        return self._access_token

    def post(self, query: str) -> Any:
        logger.debug(f"Query request: {query}")
        response = requests.get(self._authorize_url,
                                headers=self._headers,
                                json={'query': query})
        return json.loads(response.text)


def graphQL_client_from_json(path: Path = CLIENT_CREDENTIALS_PATH) -> GraphQLClient:
    with open(path, 'r') as f:
        return GraphQLClient(**json.load(f))
