import json
import random

import mongomock
import pytest

valid_partner_test_data = [{
    "id": "0",
    "tradingName": "PopCorn Station",
    "ownerName": "Dodo Dantas",
    "document": "00.000.000/000000",
    "coverageArea": {
        "type": "MultiPolygon",
        "coordinates": [
            [
                [
                    [
                        0.0,
                        0.0
                    ],
                    [
                        0.0,
                        0.0
                    ]
                ]
            ]
        ]
    },
    "address": {
        "type": "Point",
        "coordinates": [
            0.0, 0.0
        ]
    }
}]


@mongomock.patch()
@pytest.mark.parametrize("partner", valid_partner_test_data)
def test_get_partner_when_success(partner, client):
    create_response = client.post('/partners', json=partner)
    assert 201 == create_response.status_code

    partner_id = partner.get('id')
    response = client.get(f'/partners/{partner_id}')
    assert 200 == response.status_code
    assert partner == json.loads(response.data)


@mongomock.patch()
def test_get_partner_when_partner_not_found(client):
    response = client.get(f'/partners/{random.randint(0, 1000)}')
    # assert 404 == response.status_code
