"""printful Authentication."""


from base64 import b64encode
from singer_sdk.authenticators import SimpleAuthenticator


class printfulAuthenticator(SimpleAuthenticator):
    """Authenticator class for printful."""

    @classmethod
    def create_for_stream(cls, stream) -> "printfulAuthenticator":
        api_key = stream.config.get("api_key")
        encoded_key = b64encode(bytes(api_key, "utf-8")).decode("utf-8")

        return cls(
            stream=stream,
            auth_headers={
                "Authorization": f"Basic {encoded_key}"
            }
        )
