import json
from typing import List, cast
from typing_extensions import Annotated

import httpx
import pytest
import pydantic

from adminai import adminai, Asyncadminai, BaseModel
from adminai._response import (
    APIResponse,
    BaseAPIResponse,
    AsyncAPIResponse,
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    extract_response_type,
)
from adminai._streaming import Stream
from adminai._base_client import FinalRequestOptions


class ConcreteBaseAPIResponse(APIResponse[bytes]):
    ...


class ConcreteAPIResponse(APIResponse[List[str]]):
    ...


class ConcreteAsyncAPIResponse(APIResponse[httpx.Response]):
    ...


def test_extract_response_type_direct_classes() -> None:
    assert extract_response_type(BaseAPIResponse[str]) == str
    assert extract_response_type(APIResponse[str]) == str
    assert extract_response_type(AsyncAPIResponse[str]) == str


def test_extract_response_type_direct_class_missing_type_arg() -> None:
    with pytest.raises(
        RuntimeError,
        match="Expected type <class 'adminai._response.AsyncAPIResponse'> to have a type argument at index 0 but it did not",
    ):
        extract_response_type(AsyncAPIResponse)


def test_extract_response_type_concrete_subclasses() -> None:
    assert extract_response_type(ConcreteBaseAPIResponse) == bytes
    assert extract_response_type(ConcreteAPIResponse) == List[str]
    assert extract_response_type(ConcreteAsyncAPIResponse) == httpx.Response


def test_extract_response_type_binary_response() -> None:
    assert extract_response_type(BinaryAPIResponse) == bytes
    assert extract_response_type(AsyncBinaryAPIResponse) == bytes


class PydanticModel(pydantic.BaseModel):
    ...


def test_response_parse_mismatched_basemodel(client: adminai) -> None:
    response = APIResponse(
        raw=httpx.Response(200, content=b"foo"),
        client=client,
        stream=False,
        stream_cls=None,
        cast_to=str,
        options=FinalRequestOptions.construct(method="get", url="/foo"),
    )

    with pytest.raises(
        TypeError,
        match="Pydantic models must subclass our base model type, e.g. `from adminai import BaseModel`",
    ):
        response.parse(to=PydanticModel)


@pytest.mark.asyncio
async def test_async_response_parse_mismatched_basemodel(async_client: Asyncadminai) -> None:
    response = AsyncAPIResponse(
        raw=httpx.Response(200, content=b"foo"),
        client=async_client,
        stream=False,
        stream_cls=None,
        cast_to=str,
        options=FinalRequestOptions.construct(method="get", url="/foo"),
    )

    with pytest.raises(
        TypeError,
        match="Pydantic models must subclass our base model type, e.g. `from adminai import BaseModel`",
    ):
        await response.parse(to=PydanticModel)


def test_response_parse_custom_stream(client: adminai) -> None:
    response = APIResponse(
        raw=httpx.Response(200, content=b"foo"),
        client=client,
        stream=True,
        stream_cls=None,
        cast_to=str,
        options=FinalRequestOptions.construct(method="get", url="/foo"),
    )

    stream = response.parse(to=Stream[int])
    assert stream._cast_to == int


@pytest.mark.asyncio
async def test_async_response_parse_custom_stream(async_client: Asyncadminai) -> None:
    response = AsyncAPIResponse(
        raw=httpx.Response(200, content=b"foo"),
        client=async_client,
        stream=True,
        stream_cls=None,
        cast_to=str,
        options=FinalRequestOptions.construct(method="get", url="/foo"),
    )

    stream = await response.parse(to=Stream[int])
    assert stream._cast_to == int


class CustomModel(BaseModel):
    foo: str
    bar: int


def test_response_parse_custom_model(client: adminai) -> None:
    response = APIResponse(
        raw=httpx.Response(200, content=json.dumps({"foo": "hello!", "bar": 2})),
        client=client,
        stream=False,
        stream_cls=None,
        cast_to=str,
        options=FinalRequestOptions.construct(method="get", url="/foo"),
    )

    obj = response.parse(to=CustomModel)
    assert obj.foo == "hello!"
    assert obj.bar == 2


@pytest.mark.asyncio
async def test_async_response_parse_custom_model(async_client: Asyncadminai) -> None:
    response = AsyncAPIResponse(
        raw=httpx.Response(200, content=json.dumps({"foo": "hello!", "bar": 2})),
        client=async_client,
        stream=False,
        stream_cls=None,
        cast_to=str,
        options=FinalRequestOptions.construct(method="get", url="/foo"),
    )

    obj = await response.parse(to=CustomModel)
    assert obj.foo == "hello!"
    assert obj.bar == 2


def test_response_parse_annotated_type(client: adminai) -> None:
    response = APIResponse(
        raw=httpx.Response(200, content=json.dumps({"foo": "hello!", "bar": 2})),
        client=client,
        stream=False,
        stream_cls=None,
        cast_to=str,
        options=FinalRequestOptions.construct(method="get", url="/foo"),
    )

    obj = response.parse(
        to=cast("type[CustomModel]", Annotated[CustomModel, "random metadata"]),
    )
    assert obj.foo == "hello!"
    assert obj.bar == 2


async def test_async_response_parse_annotated_type(async_client: Asyncadminai) -> None:
    response = AsyncAPIResponse(
        raw=httpx.Response(200, content=json.dumps({"foo": "hello!", "bar": 2})),
        client=async_client,
        stream=False,
        stream_cls=None,
        cast_to=str,
        options=FinalRequestOptions.construct(method="get", url="/foo"),
    )

    obj = await response.parse(
        to=cast("type[CustomModel]", Annotated[CustomModel, "random metadata"]),
    )
    assert obj.foo == "hello!"
    assert obj.bar == 2
