import pytest

from ndbc_api.api.requests.http.station_metadata import MetadataRequest

TEST_STN = '41001'
STATIONS_METADATA_URL = (
    'https://www.ndbc.noaa.gov/station_page.php?station=41001')


@pytest.fixture
def stations_metadata():
    yield MetadataRequest


@pytest.mark.private
def test_historical_request(stations_metadata):
    want = STATIONS_METADATA_URL
    got = stations_metadata.build_request(TEST_STN)
    assert want == got
