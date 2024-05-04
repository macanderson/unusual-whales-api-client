from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sector_etf import SectorETF
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/market/sector-etfs",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[SectorETF, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SectorETF.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = response.text
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[SectorETF, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[SectorETF, str]]:
    """Sector Etfs

     Returns the current trading days statistics for the SPDR sector etfs

    ----
    This can be used to build a market overview such as:

    ![sectors etf](https://i.imgur.com/yQ5o6rR.png)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SectorETF, str]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[SectorETF, str]]:
    """Sector Etfs

     Returns the current trading days statistics for the SPDR sector etfs

    ----
    This can be used to build a market overview such as:

    ![sectors etf](https://i.imgur.com/yQ5o6rR.png)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SectorETF, str]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[SectorETF, str]]:
    """Sector Etfs

     Returns the current trading days statistics for the SPDR sector etfs

    ----
    This can be used to build a market overview such as:

    ![sectors etf](https://i.imgur.com/yQ5o6rR.png)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SectorETF, str]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[SectorETF, str]]:
    """Sector Etfs

     Returns the current trading days statistics for the SPDR sector etfs

    ----
    This can be used to build a market overview such as:

    ![sectors etf](https://i.imgur.com/yQ5o6rR.png)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SectorETF, str]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed