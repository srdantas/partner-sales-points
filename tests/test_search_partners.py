import json

import mongomock
import pytest


@mongomock.patch()
@pytest.mark.parametrize("lon,lat", [(1, None), (2, None)])
def test_search_partners_when_query_string_param_without_lat(client, lon, lat):
    response = client.get(f'/partners?lon={lon}')
    assert 400 == response.status_code
    assert {'message': 'Invalid request, we need lat and lon params'} == json.loads(response.data)


@mongomock.patch()
@pytest.mark.parametrize("lon,lat", [(None, 1), (None, 2)])
def test_search_partners_when_query_string_param_without_lon(client, lon, lat):
    response = client.get(f'/partners?lat={lat}')
    assert 400 == response.status_code
    assert {'message': 'Invalid request, we need lat and lon params'} == json.loads(response.data)


@mongomock.patch()
@pytest.mark.parametrize("lon,lat", [(1, 'hello'), (2, '1test')])
def test_search_partners_when_query_string_param_lat_not_is_float(client, lon, lat):
    response = client.get(f'/partners?lat={lat}a&lon={lon}')
    assert 400 == response.status_code
    assert {'message': 'Invalid request, we need lat and lon params are float values'} == json.loads(response.data)


@mongomock.patch()
@pytest.mark.parametrize("lon,lat", [('1then', 1), ('2there', 2)])
def test_search_partners_when_query_string_param_lon_not_is_float(client, lon, lat):
    response = client.get(f'/partners?lat={lat}&lon={lon}')
    assert 400 == response.status_code
    assert {'message': 'Invalid request, we need lat and lon params are float values'} == json.loads(response.data)


def test_search_partners_when_have_zero_in_coverage_area(client):
    pass


def test_search_partners_when_have_one_in_coverage_area(client):
    pass


def test_search_partners_when_have_two_in_coverage_area_then_result_is_sorted_by_address(client):
    pass


def test_search_partners_when_have_five_in_coverage_area_then_result_is_sorted_by_address(client):
    pass
