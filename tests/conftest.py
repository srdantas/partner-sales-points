import pytest

import partners


@pytest.fixture
def app():
    """Create and configure a app instance for each test."""
    yield partners.app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def valid_partner():
    return {
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
    }


@pytest.fixture
def invalid_partners():
    return [{
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
