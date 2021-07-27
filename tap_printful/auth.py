"""printful Authentication."""


from singer_sdk.authenticators import SimpleAuthenticator


class printfulAuthenticator(SimpleAuthenticator):
    """Authenticator class for printful."""

    @classmethod
    def create_for_stream(cls, stream) -> "printfulAuthenticator":
        return cls(
            stream=stream,
            auth_headers={
                "Private-Token": stream.config.get("auth_token")
            }
        )
