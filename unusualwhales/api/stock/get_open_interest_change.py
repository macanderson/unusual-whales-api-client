from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.oi_change import OIChange
from ...models.order_direction import OrderDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ticker: str,
    *,
    date: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, OrderDirection] = UNSET,
) -> Dict[str, Any]:
    # Dictionary of query parameters to be sent with the request.
    params: Dict[str, Any] = {}

    params["date"] = date

    params["limit"] = limit

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/stock/{ticker}/oi-change",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[OIChange]:
    response_json = response.json()
    if response_json.get("data") is not None:
        response_json = response_json["data"]
    if response.status_code == HTTPStatus.OK:
        response_200 = OIChange.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[OIChange]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, OrderDirection] = UNSET,
) -> Response[OIChange]:
    """OI Change

     Returns the tickers contracts' OI change data ordered by absolute OI change (default: descending).
    Date must be the current or a past date. If no date is given, returns data for the current/last
    market day.

    Args:
        ticker (str): A single ticker Example: AAPL.
        date (Union[Unset, str]): A trading date in the format of YYYY-MM-DD.
            This is optional and by default the last trading date.
             Example: 2024-01-18.
        limit (Union[Unset, int]): How many items to return. If no limit is given, returns all
            matching data. Min: 1. Example: 10.
        order (Union[Unset, OrderDirection]): Whether to sort descending or ascending. Descending
            by default. Example: asc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OIChange]
    """

    kwargs = _get_kwargs(
        ticker=ticker,
        date=date,
        limit=limit,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, OrderDirection] = UNSET,
) -> Optional[OIChange]:
    """OI Change

     Returns the tickers contracts' OI change data ordered by absolute OI change (default: descending).
    Date must be the current or a past date. If no date is given, returns data for the current/last
    market day.

    Args:
        ticker (str): A single ticker Example: AAPL.
        date (Union[Unset, str]): A trading date in the format of YYYY-MM-DD.
            This is optional and by default the last trading date.
             Example: 2024-01-18.
        limit (Union[Unset, int]): How many items to return. If no limit is given, returns all
            matching data. Min: 1. Example: 10.
        order (Union[Unset, OrderDirection]): Whether to sort descending or ascending. Descending
            by default. Example: asc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OIChange
    """

    return sync_detailed(
        ticker=ticker,
        client=client,
        date=date,
        limit=limit,
        order=order,
    ).parsed


async def asyncio_detailed(
    ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, OrderDirection] = UNSET,
) -> Response[OIChange]:
    """OI Change

     Returns the tickers contracts' OI change data ordered by absolute OI change (default: descending).
    Date must be the current or a past date. If no date is given, returns data for the current/last
    market day.

    Args:
        ticker (str): A single ticker Example: AAPL.
        date (Union[Unset, str]): A trading date in the format of YYYY-MM-DD.
            This is optional and by default the last trading date.
             Example: 2024-01-18.
        limit (Union[Unset, int]): How many items to return. If no limit is given, returns all
            matching data. Min: 1. Example: 10.
        order (Union[Unset, OrderDirection]): Whether to sort descending or ascending. Descending
            by default. Example: asc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OIChange]
    """

    kwargs = _get_kwargs(
        ticker=ticker,
        date=date,
        limit=limit,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ticker: str,
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, OrderDirection] = UNSET,
) -> Optional[OIChange]:
    """OI Change

     Returns the tickers contracts' OI change data ordered by absolute OI change (default: descending).
    Date must be the current or a past date. If no date is given, returns data for the current/last
    market day.

    Args:
        ticker (str): A single ticker Example: AAPL.
        date (Union[Unset, str]): A trading date in the format of YYYY-MM-DD.
            This is optional and by default the last trading date.
             Example: 2024-01-18.
        limit (Union[Unset, int]): How many items to return. If no limit is given, returns all
            matching data. Min: 1. Example: 10.
        order (Union[Unset, OrderDirection]): Whether to sort descending or ascending. Descending
            by default. Example: asc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OIChange
    """

    return (
        await asyncio_detailed(
            ticker=ticker,
            client=client,
            date=date,
            limit=limit,
            order=order,
        )
    ).parsed
