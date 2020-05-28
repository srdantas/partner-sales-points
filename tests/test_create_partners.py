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

invalid_partner_test_data = [{
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
},
    {
        "id": "0",
        "tradingName": "PopCorn Station",
        "ownerName": "Dodo Dantas",
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
    },
    {
        "id": "0",
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
    },
    {
        "id": "0",
        "tradingName": "PopCorn Station",
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
    },
    {
        "id": "0",
        "tradingName": "PopCorn Station",
        "ownerName": "Dodo Dantas",
        "document": "00.000.000/000000",
        "address": {
            "type": "Point",
            "coordinates": [
                0.0, 0.0
            ]
        }
    },
    {
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
        }
    },
    {
        "id": "0",
        "tradingName": "PopCorn Station",
        "ownerName": "Dodo Dantas",
        "document": "00.000.000/000000",
        "coverageArea": {
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
    },
    {
        "id": "0",
        "tradingName": "PopCorn Station",
        "ownerName": "Dodo Dantas",
        "document": "00.000.000/000000",
        "coverageArea": {
            "type": "MultiPolygon"
        },
        "address": {
            "type": "Point",
            "coordinates": [
                0.0, 0.0
            ]
        }
    },
    {
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
            "coordinates": [
                0.0, 0.0
            ]
        }
    },
    {
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
            "type": "Point"
        }
    }]


@mongomock.patch()
@pytest.mark.parametrize("partner", valid_partner_test_data)
def test_create_partner_when_success(partner, client):
    response = client.post('/partners', json=partner)
    assert 201 == response.status_code
    assert b'' == response.data


@mongomock.patch()
@pytest.mark.parametrize("partner", valid_partner_test_data)
def test_create_partner_when_duplicated_document(partner, client):
    response = client.post('/partners', json=partner)
    assert 201 == response.status_code

    # change id, because this is unique
    partner['id'] = str(random.randint(1, 1000))

    second_response = client.post('/partners', json=partner)
    assert 400 == second_response.status_code
    assert {'message': 'This document already exists in database'} == json.loads(second_response.data)


@mongomock.patch()
@pytest.mark.parametrize("partner", valid_partner_test_data)
def test_create_partner_when_duplicated_id(partner, client):
    response = client.post('/partners', json=partner)
    assert 201 == response.status_code

    second_response = client.post('/partners', json=partner)
    assert 400 == second_response.status_code
    assert {'message': 'This id already exists in database'} == json.loads(response.data)


@mongomock.patch()
@pytest.mark.parametrize("partner", invalid_partner_test_data)
def test_create_partner_when_invalid_payload_schema(partner, client):
    response = client.post('/partners', json=partner)
    assert 400 == response.status_code
    assert {'message': 'Invalid payload'} == json.loads(response.data)
