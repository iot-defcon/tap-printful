"""REST client handling, including printfulStream base class."""

import requests
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream
from tap_printful.auth import printfulAuthenticator


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class printfulStream(RESTStream):
    """printful stream class."""

    url_base = "https://api.printful.com/"

    records_jsonpath = "$.result[*]"
    offset_jsonpath = "$.paging.offset"
    limit_jsonpath = "$.paging.limit"
    total_pages_jsonpath = "$.paging.total"

    @property
    def authenticator(self) -> printfulAuthenticator:
        """Return a new authenticator object."""
        return printfulAuthenticator.create_for_stream(self)

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        return {}

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""

        all_matches = extract_jsonpath(self.total_pages_jsonpath, input=response.json())
        total_pages = next(iter(all_matches), None)

        all_matches = extract_jsonpath(self.offset_jsonpath, input=response.json())
        offset = next(iter(all_matches), None)

        all_matches = extract_jsonpath(self.limit_jsonpath, input=response.json())
        limit = next(iter(all_matches), None)

        next_offset = int(offset) + int(limit)

        if next_offset >= int(total_pages) * int(limit):
            return None

        return next_offset

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}

        if next_page_token:
            params["offset"] = next_page_token

        return params

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())