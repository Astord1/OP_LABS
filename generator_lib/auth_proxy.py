import requests
import time
from typing import Callable, Optional


class AuthStrategy:
    def inject(self, headers: dict) -> dict:
        return headers


class ApiKeyAuth(AuthStrategy):
    def __init__(self, key: str, header_name: str = "Authorization"):
        self.key = key
        self.header_name = header_name

    def inject(self, headers: dict) -> dict:
        headers[self.header_name] = f"ApiKey {self.key}"
        return headers


class JwtAuth(AuthStrategy):
    def __init__(self, token_provider: Callable[[], str]):
        self.token_provider = token_provider

    def inject(self, headers: dict) -> dict:
        token = self.token_provider()
        headers["Authorization"] = f"Bearer {token}"
        return headers


class AuthProxy:
    def __init__(self, auth_strategy: AuthStrategy, base_url: str, log: Optional[Callable[[str], None]] = None):
        self.auth_strategy = auth_strategy
        self.base_url = base_url.rstrip("/")
        self.log = log or (lambda msg: None)

    def request(self, method: str, endpoint: str, **kwargs):
        headers = kwargs.pop("headers", {})
        headers = self.auth_strategy.inject(headers)

        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        self.log(f"[AuthProxy] {method.upper()} {url} HEADERS={headers}")
        response = requests.request(method, url, headers=headers, **kwargs)
        return response
