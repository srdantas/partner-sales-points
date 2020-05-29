import json
import random

import pytest


def test_create_partner_when_success(valid_partner, client):
    response = client.post('/partners', json=valid_partner)
    assert 201 == response.status_code
    assert b'' == response.data


def test_create_partner_when_duplicated_document(valid_partner, client):
    response = client.post('/partners', json=valid_partner)
    assert 201 == response.status_code

    # change id, because this is unique
    valid_partner['id'] = str(random.randint(1, 1000))

    second_response = client.post('/partners', json=valid_partner)
    assert 400 == second_response.status_code
    assert {'message': 'Id or document already exists in database'} == json.loads(second_response.data)


def test_create_partner_when_duplicated_id(valid_partner, client):
    response = client.post('/partners', json=valid_partner)
    assert 201 == response.status_code

    second_response = client.post('/partners', json=valid_partner)
    assert 400 == second_response.status_code
    assert {'message': 'Id or document already exists in database'} == json.loads(second_response.data)


def test_create_partner_when_invalid_payload_schema(invalid_partners, client):
    for partner in invalid_partners:
        response = client.post('/partners', json=partner)
        assert 400 == response.status_code
        assert {'message': 'Invalid payload'} == json.loads(response.data)


def test_get_partner_when_success(valid_partner, client):
    create_response = client.post('/partners', json=valid_partner)
    assert 201 == create_response.status_code

    partner_id = valid_partner.get('id')
    response = client.get(f'/partners/{partner_id}')
    assert 200 == response.status_code
    assert valid_partner == json.loads(response.data)


def test_get_partner_when_partner_not_found(client):
    response = client.get(f'/partners/{random.randint(0, 1000)}')
    assert 404 == response.status_code


@pytest.mark.parametrize("lon,lat", [(1, None), (2, None)])
def test_search_partners_when_query_string_param_without_lat(client, lon, lat):
    response = client.get(f'/partners?lon={lon}')
    assert 400 == response.status_code
    assert {'message': 'Invalid request, we need lat and lon params'} == json.loads(response.data)


@pytest.mark.parametrize("lon,lat", [(None, 1), (None, 2)])
def test_search_partners_when_query_string_param_without_lon(client, lon, lat):
    response = client.get(f'/partners?lat={lat}')
    assert 400 == response.status_code
    assert {'message': 'Invalid request, we need lat and lon params'} == json.loads(response.data)


@pytest.mark.parametrize("lon,lat", [(1, 'hello'), (2, '1test')])
def test_search_partners_when_query_string_param_lat_not_is_float(client, lon, lat):
    response = client.get(f'/partners?lat={lat}a&lon={lon}')
    assert 400 == response.status_code
    assert {'message': 'Invalid request, we need lat and lon params are float values'} == json.loads(response.data)


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
