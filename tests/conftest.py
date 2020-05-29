import os

import pytest
import testcontainers.compose

import partners
import tests.generators

COMPOSE_PATH = os.path.dirname(os.path.abspath(__name__))


@pytest.yield_fixture(autouse=True, scope='module')
def compose_start():
    """Setup a compose with dependencies for tests."""
    compose = testcontainers.compose.DockerCompose(COMPOSE_PATH)
    compose.start()
    yield compose


@pytest.yield_fixture(autouse=True, scope='session')
def test_suite_cleanup_thing():
    yield


@pytest.yield_fixture
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
        "id": tests.generators.generate_id(),
        "tradingName": "PopCorn Station",
        "ownerName": "Dodo Dantas",
        "document": tests.generators.generate_document(),
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
                            1.0,
                            1.0
                        ],
                        [
                            2.0,
                            2.0
                        ],
                        [
                            0.0,
                            0.0
                        ],
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
        "document": tests.generators.generate_document(),
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
                            1.0,
                            1.0
                        ],
                        [
                            2.0,
                            2.0
                        ],
                        [
                            0.0,
                            0.0
                        ],
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
            "id": tests.generators.generate_id(),
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
                                1.0,
                                1.0
                            ],
                            [
                                2.0,
                                2.0
                            ],
                            [
                                0.0,
                                0.0
                            ],
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
            "id": tests.generators.generate_id(),
            "ownerName": "Dodo Dantas",
            "document": tests.generators.generate_document(),
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
                                1.0,
                                1.0
                            ],
                            [
                                2.0,
                                2.0
                            ],
                            [
                                0.0,
                                0.0
                            ],
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
            "id": tests.generators.generate_id(),
            "tradingName": "PopCorn Station",
            "document": tests.generators.generate_document(),
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
                                1.0,
                                1.0
                            ],
                            [
                                2.0,
                                2.0
                            ],
                            [
                                0.0,
                                0.0
                            ],
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
            "id": tests.generators.generate_id(),
            "tradingName": "PopCorn Station",
            "ownerName": "Dodo Dantas",
            "document": tests.generators.generate_document(),
            "address": {
                "type": "Point",
                "coordinates": [
                    0.0, 0.0
                ]
            }
        },
        {
            "id": tests.generators.generate_id(),
            "tradingName": "PopCorn Station",
            "ownerName": "Dodo Dantas",
            "document": tests.generators.generate_document(),
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
                                1.0,
                                1.0
                            ],
                            [
                                2.0,
                                2.0
                            ],
                            [
                                0.0,
                                0.0
                            ],
                        ]
                    ]
                ]
            }
        },
        {
            "id": tests.generators.generate_id(),
            "tradingName": "PopCorn Station",
            "ownerName": "Dodo Dantas",
            "document": tests.generators.generate_document(),
            "coverageArea": {
                "coordinates": [
                    [
                        [
                            [
                                0.0,
                                0.0
                            ],
                            [
                                1.0,
                                1.0
                            ],
                            [
                                2.0,
                                2.0
                            ],
                            [
                                0.0,
                                0.0
                            ],
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
            "id": tests.generators.generate_id(),
            "tradingName": "PopCorn Station",
            "ownerName": "Dodo Dantas",
            "document": tests.generators.generate_document(),
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
            "id": tests.generators.generate_id(),
            "tradingName": "PopCorn Station",
            "ownerName": "Dodo Dantas",
            "document": tests.generators.generate_document(),
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
                                1.0,
                                1.0
                            ],
                            [
                                2.0,
                                2.0
                            ],
                            [
                                0.0,
                                0.0
                            ],
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
            "id": tests.generators.generate_id(),
            "tradingName": "PopCorn Station",
            "ownerName": "Dodo Dantas",
            "document": tests.generators.generate_document(),
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
                                1.0,
                                1.0
                            ],
                            [
                                2.0,
                                2.0
                            ],
                            [
                                0.0,
                                0.0
                            ],
                        ]
                    ]
                ]
            },
            "address": {
                "type": "Point"
            }
        }]
