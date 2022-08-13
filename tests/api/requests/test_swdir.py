import yaml

import pytest

from ndbc_api.api.requests.swdir import SwdirRequest
from tests.api.requests._base import (
    REALTIME_START,
    REALTIME_END,
    HISTORICAL_START,
    HISTORICAL_END,
    REQUESTS_TESTS_DIR,
)


TEST_FP = REQUESTS_TESTS_DIR.joinpath('swdir.yml')
TEST_STN = '41001'


@pytest.fixture
def swdir():
    yield SwdirRequest


@pytest.fixture
def swdir_requests():
    with open(TEST_FP, 'r') as f:
        data = yaml.safe_load(f)
    yield data


@pytest.fixture
def swdir_realtime_requests(swdir_requests):
    yield swdir_requests.get('realtime')


@pytest.fixture
def swdir_historical_requests(swdir_requests):
    yield swdir_requests.get('historical')


def test_swdir_realtime(swdir, swdir_realtime_requests):
    want = swdir_realtime_requests
    got = swdir.build_request(TEST_STN, REALTIME_START, REALTIME_END)
    assert want == got


def test_swdir_historical(swdir, swdir_historical_requests):
    want = swdir_historical_requests
    got = swdir.build_request(TEST_STN, HISTORICAL_START, HISTORICAL_END)
    assert want == got
