import netCDF4 as nc

import pytest

from ndbc_api.api.parsers.opendap.adcp import AdcpParser
from tests.api.parsers.opendap._base import PARSED_TESTS_DIR, RESPONSES_TESTS_DIR

TEST_FP = RESPONSES_TESTS_DIR.joinpath('adcp.content')
PARSED_FP = PARSED_TESTS_DIR.joinpath('adcp.nc')


@pytest.fixture
def adcp_response():
    with open(TEST_FP, 'rb') as f:
        data = f.read()
    yield data


@pytest.fixture
def parsed_adcp():
    ds = nc.Dataset(PARSED_FP, 'r')
    yield ds


@pytest.fixture
def adcp():
    yield AdcpParser


@pytest.mark.private
def test_available_measurements(adcp, adcp_response, parsed_adcp):
    resp = adcp_response
    want = parsed_adcp
    got = adcp.nc_from_responses([resp])
    assert set(want.variables.keys()) == set(got.variables.keys())

