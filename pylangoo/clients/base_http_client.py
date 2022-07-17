"""
file: base_http_client.py
description: Base class for HTTP Python Clients
"""
from typing import List, Union

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def either(tp, err_tp):
    def parser(json: dict) -> Union[err_tp, tp, List[tp]]:
        if "code" in json and json["code"] != 200:
            return err_tp(**json)
        else:
            if isinstance(json, list):
                return [tp(**j) for j in json]
            return tp(**json)

    return parser


class HTTPClientException(Exception):
    @classmethod
    def create_from_response(cls, response):
        """The default implementation to create exceptions from response object.

        If the client is interacting with an API which has different interface, this method
        should be overridden to match with the response that is returned by the API.
        """
        parsed_response = response.json()
        try:
            message = "Server returned status {}, code {}: {}".format(
                response.status_code,
                parsed_response["code"],
                parsed_response["message"],
            )
        except Exception:
            message = "Server returned status {}".format(response.status_code)

        return cls(message)


class BaseHTTPClient:
    """Client class for interacting with HTTP endpoints."""

    def __init__(self, host, port):
        """Creates a BaseHTTPClient.

        Args:
            host (str): client host (e.g. localhost)
            port (int): client port
        """
        if not any(host.startswith(prefix) for prefix in ["http://", "https://"]):
            host = "http://" + host
        else:
            prefix = "https://" if "https://" in host else "http://"
        self.base_url = "{}:{}".format(host, port)

        # Define a request session and configure it so that all outbound http
        # traffic has exponential backoff retries
        self.sess = requests.Session()
        retry_strategy = Retry(
            total=5, backoff_factor=0.1, status_forcelist=[502, 503, 504]
        )
        self.sess.mount(prefix, HTTPAdapter(max_retries=retry_strategy))

    def do_request(
        self,
        method,
        url,
        operation_name,
        headers=None,
        data=None,
        params=None,
        json=None,
        client_exception_class=None,
        timeout=None,
    ):
        """Convenience method to do requests.

        Args:
            method (str): http method, such as "POST, "GET", etc.
            url (str): request url
            operation_name (str): name for the operation for tracing
            headers (dict): request headers
            data (Optional[dict]): request data to be sent
            params (Optional[dict]): request params to be sent
            json (Optional[dict]): json to send in the body of the request
            client_exception_class (type): The type of exception to be raised
                on an error (expected to inherit from HTTPClientException)
            timeout (float or tuple): How long to wait for the server to send
                data before giving up, as a float, or a :ref:`(connect timeout,
                read timeout) <timeouts>` tuple.

        Returns:
            Deserialized JSON response, or resp.text if empty (204)

        Raises:
            HTTPClientException: if requests fails or there's an error
            TypeError: if the client_exception_class does not inherit from
                HTTPClientException
        """
        client_exception_class = client_exception_class or HTTPClientException
        if not issubclass(client_exception_class, HTTPClientException):
            raise TypeError(
                "client_exception_class:{} does not inherit "
                "from HTTPClientException".format(type(client_exception_class))
            )
        try:
            resp = self.sess.request(
                method,
                url,
                headers=headers,
                data=data,
                params=params,
                json=json,
                timeout=timeout,
            )
            if int(resp.status_code) // 100 != 2:
                raise client_exception_class.create_from_response(resp)
            elif resp.status_code == 204:
                return resp.text
            return resp.json()
        except client_exception_class as e:
            raise e
        except Exception as e:
            raise client_exception_class(
                "Error in {}: {}".format(operation_name, str(e))
            ) from e
