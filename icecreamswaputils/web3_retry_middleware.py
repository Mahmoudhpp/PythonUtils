from time import sleep
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Collection,
    Type,
)

from requests.exceptions import (
    ConnectionError,
    HTTPError,
    Timeout,
    TooManyRedirects,
)
from web3 import HTTPProvider
from web3.middleware.exception_retry_request import check_if_retry_on_failure

from web3.types import (
    RPCEndpoint,
    RPCResponse,
)

RPC_NON_RETRY_ERROR_RESPONSES = [
    "reverted",
    "out of gas"
]


class RPCError(Exception):
    """An RPC error response was received."""


def web3_http_exponential_delay_retry_request_middleware(
    errors: Collection[Type[BaseException]] = (RPCError, ConnectionError, HTTPError, Timeout, TooManyRedirects),
    retries: int = 7,
    initial_delay_s=1,
):
    def create_middleware(make_request: Callable[[RPCEndpoint, Any], Any], w3) -> Callable[[RPCEndpoint, Any], Any]:
        def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
            if check_if_retry_on_failure(method):
                for i in range(retries):
                    try:
                        response = make_request(method, params)
                        if "error" in response and i < retries - 1 and not any(message in response["error"]["message"].lower() for message in RPC_NON_RETRY_ERROR_RESPONSES):
                            print(f"RPC got Error response, retrying: {response['error']}")
                            raise RPCError(response['error'])
                        return response
                    # https://github.com/python/mypy/issues/5349
                    except errors:  # type: ignore
                        if i < retries - 1:
                            sleep(initial_delay_s * 2**i)
                            continue
                        else:
                            raise
                raise Exception(f"web3_http_exponential_delay_retry_request_middleware with 0 retries")
            else:
                return make_request(method, params)

        return middleware

    return create_middleware
