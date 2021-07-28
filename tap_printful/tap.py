"""printful tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_printful.streams import (
    OrdersStream
)

STREAM_TYPES = [
    OrdersStream
]


class Tapprintful(Tap):
    """printful tap class."""
    name = "tap-printful"

    config_jsonschema = th.PropertiesList(
        th.Property("api_key", th.StringType, required=True),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
