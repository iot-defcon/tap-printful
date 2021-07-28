"""Printful tap class."""

from typing import List

from pathlib import PurePath
from singer_sdk import Tap, Stream
from singer_sdk import typing as th
from tap_printful.streams import OrdersStream
from typing import List, Optional, Union

STREAM_TYPES = [OrdersStream]


class TapPrintful(Tap):
    """Printful tap class."""

    name = "tap-printful"

    config_jsonschema = th.PropertiesList(
        th.Property("api_key", th.StringType, required=True),
    ).to_dict()

    def __init__(
        self,
        config: Optional[Union[dict, PurePath, str, List[Union[PurePath, str]]]] = None,
        catalog: Union[PurePath, str, dict, None] = None,
        state: Union[PurePath, str, dict, None] = None,
        parse_env_config: bool = False,
    ) -> None:
        super().__init__(
            config=config, catalog=catalog, state=state, parse_env_config=True
        )

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
